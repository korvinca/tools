#!/usr/bin/env python3

"""
:description:
this script retrieves variables values from an artifactory manifest (maven)
and extracts the values for a particular project version. It updates the inputset
of a given pipeline.
:caveats:
the inputset must exist for the script to update it successfully.
param project-version: artifact version in maven
param config: yaml configuration file (default: config.yml)
"""

import argparse
import glob
import json
import logging
import os
import re
import sys
import zipfile
from typing import Any, Dict, List

import hvac
import requests
import yaml
from dotenv import load_dotenv
from packaging import version
from requests_toolbelt.utils import dump

logging.basicConfig(level=logging.DEBUG)

load_dotenv()


class OV:
    def __init__(self, params: Dict[str, Any]) -> None:
        """
        :description: initialize internal variables that functions will use
        :param params: Dict with parameter values
        :return: none
        """

        self.config = params["config"]
        self.version = params["version"]
        self.jenkins = False

        with open(self.config, "r", encoding="utf-8") as f:
            data_str = f.read()
            self.data = yaml.safe_load(data_str)
            print(json.dumps(self.data, indent=4))
        self.data["vault"]["token"] = os.getenv("VAULT_TOKEN")
        if os.getenv("BUILD_NUMBER"):
            self.jenkins = True
        self.data["manifest"]["version"] = self.version

    def vault_secrets(self) -> None:
        """
        :description: retrieve harness secrets and update Dict
        :param: none
        :return: none
        """

        logging.debug("vault_secrets()")
        self.check_notnull("vault", ["token"])
        if not self.data["vault"]["token"]:
            print("VAULT_TOKEN is not defined. exiting.")
            sys.exit(1)
        client = hvac.Client(
            url=self.data["vault"]["addr"],
            namespace=self.data["vault"]["namespace"],
            token=self.data["vault"]["token"],
        )
        assert client.is_authenticated()
        d = client.secrets.kv.v1.read_secret(
            mount_point=self.data["vault"]["secretmount"],
            path=self.data["vault"]["secretpath"],
        )
        try:
            self.data["harness"]["account"] = d["data"]["account"]
            self.data["harness"]["apikey"] = d["data"]["apikey"]
        except KeyError:
            print("Could not retrieve secrets from vault.")
            sys.exit(1)

    def download_url(self, url: str, save_path: str, chunk_size: int = 128) -> None:
        """
        :description: download file from url
        :param url: url of the file to fetch
        :param save_path: where to save the file
        :param chunk_size: stream buffer size
        :return: none
        """

        r = requests.get(url, stream=True, allow_redirects=True)
        with open(save_path, "wb") as fd:
            for chunk in r.iter_content(chunk_size=chunk_size):
                fd.write(chunk)

    def merge_yaml(self, fList: List[str]) -> Dict[str, Any]:
        """
        :description: takes a List of yaml files and loads them as a single yaml document.
            restrictions:
            1) None of the files may have a yaml document marker (---)
            2) All of the files must have the same top-level type (Dictionary or List)
            3) If any pointers cross between files, then the file in which they are defined (&) must be
            earlier in the List than any uses (*).
        :param fList: List of yaml files
        :return: python Dict representing merged yaml files
        """
        if not fList:
            # if flist is the empty List, return an empty List. This is arbitrary, if it turns out that
            # an empty Dictionary is better, we can do something about that.
            return {}
        sList: List[str] = []
        for f in fList:
            with open(f, "r") as stream:
                sList.append(stream.read())
        fString: str = ""
        for s in sList:
            fString = fString + "\n" + s
        y: Dict[str, Any] = yaml.safe_load(fString)
        return y

    def extract_keys(self, parentdir: str, fregex: str) -> Dict[str, str]:
        """
        :description: returns Dict with k,v wanted from yaml file
            restrictions:
            1) each value is a key, value what are simple strings
        :param parentdir: parent dir path where the files are located
        :param fregex: yaml file pattern regex
        :return Dict[str, str]: map with k,v pairs
        """

        logging.debug("extract_keys()")
        values: Dict[str, str] = {}
        f: str = parentdir + "/*" + fregex + "*"

        yamlfiles: List[str] = glob.glob(f)
        vars: Dict[str, str] = self.merge_yaml(yamlfiles)

        for k in self.data["manifest"]["keys"]:
            values[k] = vars[k]

        return values

    def check_notnull(self, component: str, items: List[str]) -> None:
        """
        :description: verify that values are not null
        :param component: primary map key in self.data
        :param items: List of string value representing secondary key in self.data
        :return: none
        """
        for item in items:
            if not self.data[component][item]:
                print(" ".join(["missing variable", item, "in", component]))
                sys.exit(1)

    def manifest_vars(self) -> None:
        """
        :description: retrieve key/value from manifest artifact zip manifest
        :param: none
        :return Dict: Dict of k/v string
        """

        logging.debug("manifest_vars()")
        self.check_notnull("manifest", ["name", "component", "regex"])

        # get content
        try:
            url = "/".join(
                [
                    self.data["manifest"]["url"],
                    self.data["manifest"]["name"],
                    self.data["manifest"]["component"],
                    "/",
                ]
            )
            url = re.sub(r"//$", "/", url)
            r = requests.get(url, allow_redirects=True)
            if r.status_code != 200:
                dd = dump.dump_all(r)
                logging.debug(dd.decode("utf-8"))
                raise Exception("failed to fetch manifest")
            self.data["manifest"]["content"] = r.text
        except KeyError:
            print("name, component, or regex is invalid")
            sys.exit(1)

        if self.data["manifest"]["version"] in ["latest", ""]:
            print(self.data["manifest"]["url"])
            m = re.findall(r'href="(\d[\d|\-|\.]+\d)', self.data["manifest"]["content"])
            found: List[str] = sorted(m, key=lambda x: version.Version(x))
            print(found)
            self.data["manifest"]["version"] = found[-1]
        if not self.data["harness"]["inputset"]:
            self.data["harness"]["inputset"] = "-".join(
                [
                    self.data["manifest"]["component"],
                    self.data["manifest"]["version"],
                ]
            )
        zipfilename: str = "-".join(
            [
                self.data["manifest"]["component"],
                self.data["manifest"]["version"],
                "resources.zip",
            ]
        )
        zipfilepath: str = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            self.data["manifest"]["tmpdir"],
        )
        url = "/".join(
            [
                self.data["manifest"]["url"],
                self.data["manifest"]["name"],
                self.data["manifest"]["component"],
                self.data["manifest"]["version"],
                zipfilename,
            ]
        )
        if not os.path.exists(zipfilepath):
            os.mkdir(zipfilepath)
        zipfullpath: str = os.path.join(zipfilepath, zipfilename)
        self.download_url(url, os.path.join(zipfilepath, zipfilename))
        with zipfile.ZipFile(zipfullpath, "r") as zip_ref:
            zip_ref.extractall(zipfilepath)

        parentdir: str = os.path.join(
            zipfilepath,
            "-".join(
                [self.data["manifest"]["component"], self.data["manifest"]["version"]]
            ),
        )
        self.data["manifest"]["variables"] = self.extract_keys(
            parentdir, self.data["manifest"]["regex"]
        )
        logging.debug(json.dumps(self.data["manifest"]["variables"], indent=4))

    def harness_inputset(self, extras: Dict[str, Any]) -> None:
        """
        :description: update inputset with manifest vars
        :param extras: list of extra inputsets
        :return Dict: inputset record
        """

        logging.debug("harness_inputset()")
        self.check_notnull(
            "harness", ["apikey", "account", "pipeline", "project", "org"]
        )
        headers: Dict[str, str] = {
            "x-api-key": self.data["harness"]["apikey"],
            "Content-Type": "application/yaml",
        }

        params: Dict[str, str] = {
            "accountIdentifier": self.data["harness"]["account"],
            "orgIdentifier": self.data["harness"]["org"],
            "projectIdentifier": self.data["harness"]["project"],
            "pipelineIdentifier": self.data["harness"]["pipeline"],
        }

        inputset_id = self.data["harness"]["inputset"]
        inputset_id = inputset_id.replace("-", "")

        payload: Dict[str, Any] = {
            "inputSet": {
                "identifier": inputset_id,
                "name": self.data["harness"]["inputset"],
                "tags": {},
                "orgIdentifier": self.data["harness"]["org"],
                "projectIdentifier": self.data["harness"]["project"],
                "pipeline": {
                    "identifier": self.data["harness"]["pipeline"],
                    "variables": [],
                },
            }
        }

        for k, v in extras.items():
            self.data["manifest"]["variables"][k] = v
        for k, v in self.data["manifest"]["variables"].items():
            payload["inputSet"]["pipeline"]["variables"].append(
                {
                    "name": k,
                    "type": "String",
                    "value": v,
                }
            )
        yaml_data: str = yaml.dump(payload)

        url = "/".join(
            [
                self.data["harness"]["url"],
                self.data["harness"]["inputset"],
            ]
        )

        r = requests.put(
            url,
            params=params,
            headers=headers,
            data=yaml_data,
        )
        if r.status_code != 200:
            dd = dump.dump_all(r)
            logging.debug(dd.decode("utf-8"))
            raise Exception("failed to make harness api call")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Retrieve vars from manifest and add them to harness."
    )
    parser.add_argument(
        "-c",
        "--config",
        default="config.yml",
        help="yaml configuration file",
    )
    parser.add_argument(
        "-v",
        "--version",
        default="",
        help="manifest version",
    )
    parser.add_argument(
        "-e",
        "--env-name",
        default="",
        help="environment name",
    )
    parser.add_argument(
        "-i",
        "--harness-inputset",
        default="",
        required=True,
        help="Harness inputset id",
    )

    parser.add_argument(
        "-p",
        "--harness-project",
        default="",
        required=True,
        help="Harness project id",
    )
    parser.add_argument(
        "-q",
        "--harness-pipeline",
        default="",
        required=True,
        help="Harness pipeline id",
    )
    args = parser.parse_args()

    params = {
        "config": args.config,
        "version": args.version,
        "harness_pipeline": args.harness_pipeline,
        "harness_project": args.harness_project,
        "harness_inputset": args.harness_inputset,
    }

    extra_inputs: Dict[str, Any] = {"env_name": args.env_name}
    o = OV(params)
    o.vault_secrets()
    o.manifest_vars()
    o.harness_inputset(extra_inputs)

    sys.exit(0)
