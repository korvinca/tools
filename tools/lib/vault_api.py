#!/usr/bin/python3

import os
import json
import argparse
import requests
import yaml


yaml.warnings({'YAMLLoadWarning': False})

def get_sub_item(_long_string, _item):
    """Subtract substring from a long string"""
    start_pos = _long_string.find(_item)
    if start_pos == -1:
        return ""
    end_pos = _long_string.find('\n', start_pos)
    while end_pos != -1 and _long_string[end_pos+1] == ' ':
        end_pos = _long_string.find("\n", end_pos+1)
    return _long_string[start_pos:end_pos] if end_pos != -1 else _long_string[start_pos:]

class VaultAPI(object):
    """Get and post key:value to Vault"""
    def __init__(self, options):
        """Initialize environment variables"""
        if not options.server or not options.token or not options.path:
            raise Exception("Server, token and path must be provided.")
        else:
            self.headers = {'X-Vault-Token': options.token}
            self.headers_post = {'X-Vault-Token': options.token, 'Content-Type': 'application/json'}
            self.address = options.server + "/v1/" + options.path
            self.key = None
            self.item = None
            self.value = None
            self.secret = False
        if options.key:
            self.key = options.key
        if options.item:
            self.item = options.item
        if options.value:
            self.value = options.value
        if options.secret:
            self.secret = True
        if not os.path.exists("../../target"):
            os.makedirs("../../target")
            open("../../target/placeholder", "a").close()
        print("\nSecret path is:", options.path)

    def list_secret(self):
        """LIST all the secret under a certain path"""
        res = requests.request(method="list", url=self.address, headers=self.headers)
        if res.status_code == 200:
            secret_list = res.json()['data']['keys']
        else:
            secret_list = ""
        index = 0
        for item in secret_list:
            secret_list[index] = self.address + item
            index += 1
        return secret_list

    def get_secret(self):
        """GET a secret from Vault"""
        if self.address[-1] != '/':
            iteration_list = self.address.split()
        else:
            iteration_list = self.list_secret()
        for index in iteration_list:
            if self.address[-1] == '/':
                print("\nSecret path is: " + index.split('v1/')[1])
            res = requests.get(url=index, headers=self.headers)
            if res.status_code == 200:
                secret = res.json()['data']
                if self.secret and self.address[-1] != '/':
                    with open("../../target/" + index.split('/')[-1] + ".yml", "a") as key_file:
                        y_data = yaml.dump(yaml.load(json.dumps(secret)))
                        print("Environment:\n", y_data)
                        key_file.write(str(y_data))
                elif self.secret and self.address[-1] == '/':
                    with open("../../target/" + index.split('/')[-1] + ".yml", "a") as key_file:
                        y_data = yaml.dump(yaml.load(json.dumps(secret)))
                        print("Environment:\n", y_data)
                        key_file.write(str(y_data))
                elif not self.secret:
                    for key in secret.keys():
                        key_value = res.json()['data'][key]
                        if self.item is None:
                            with open("../../target/" + key + ".yml", "a") as key_file:
                                print("Key:", key)
                                print("Value:\n", key_value)
                                if self.address[-1] == '/':
                                    key_file.write(str("\n\nsecret_path: " \
                                        + index.split('v1/')[1]) + "\n")
                                key_file.write(str(key_value))
                        else:
                            with open("../../target/" + index.split('/')[-1] + "_" + \
                                key + ".yml", "w") as key_file:
                                for item in self.item.split(','):
                                    item_line = get_sub_item(key_value, item)
                                    print(item_line)
                                    key_file.write(str(item_line)+'\n')
            else:
                print("No secret in Vault. You need to POST secret before.")

    def post_secret(self):
        """POST a secret to Vault"""
        if self.key:
            if self.key == "all":
                print("Do not use dummy key name 'all'!!!\n")
                raise SystemExit
            res = requests.get(url=self.address, headers=self.headers)
            if res.status_code == 200:
                secret = res.json()['data']
                secret.update({self.key: self.value})
                s_data = json.dumps(secret)
            else:
                s_data = json.dumps({self.key: self.value})
        else:
            s_data = json.dumps(yaml.load(self.value, Loader=yaml.FullLoader))
        requests.post(url=self.address, data=s_data, headers=self.headers_post)


def parse_args():
    """Parse command line arguments from sys.argv.
    Run script with--help to see the valid options.
    python vault_api.py -s <http://url:port> -t <token> -p <path to secret> -k <key> -v <value>
    """
    desc = """Script performs command on server via ssh connection"""
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-s", "--server",
                        help="Vault server ")
    parser.add_argument("-t", "--token",
                        help="Vault token")
    parser.add_argument("-p", "--path",
                        help="Path to secret")
    parser.add_argument("-k", "--key",
                        help="secret key")
    parser.add_argument("-v", "--value",
                        help="secret value")
    parser.add_argument("-i", "--item",
                        help="key item")
    parser.add_argument("-a", "--secret",
                        help="get all secret",
                        action='store_true')
    return parser.parse_args()


if __name__ == '__main__':
    OPTIONS = parse_args()
    VAULT = VaultAPI(OPTIONS)
    if not OPTIONS.value:
        VAULT.get_secret()
    else:
        VAULT.post_secret()
        VAULT.get_secret()