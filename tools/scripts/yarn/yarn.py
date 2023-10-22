#!/usr/bin/python3
"""
Arguments:
arg_state = [to be preloaded, preloaded, preloading, failed, testing]
arg_release = "new_project"
arg_release_version = "0.1"
arg_type = [ova, vanilla, lite]
arg_pool = [static, dynamic]
arg_leased = [0,1]
"""

import json
import random
import common
import argparse


class ActionYARN(object):
    """Get key:value from json file"""
    def __init__(self, options):
        """Initialize environment variables"""
        if not options.file :
            raise Exception("JSON file with data must be provided!!!")
        else:
            self.environment = None
            self.state = None
            self.version = None
            self.type = False
            self.pool = False
            self.lease = 0
        if options.environment:
            self.env_name = options.environment
        if options.state:
            self.state = options.state
        if options.release :
            self.release = options.release
        if options.release :
            self.version = options.version
        if options.type :
            self.type = options.type
        if options.pool :
            self.pool = options.pool
        if options.lease :
            self.lease = options.lease
        if options.array :
            self.array = options.array
        # Opening JSON file
        with open(options.file) as json_file:
            self.data = json.load(json_file)

    def get_env_item(self):
        env_list = common.get_preloaded(self.data,self.state,
                self.release,self.version,self.type,self.pool,self.lease)
        if env_list :
            self.env_name = random.choice(env_list)
            print("Pool of available environments:", env_list)
            f = open( '_env_name.txt', 'w' )
            f.write( 'export ENV_NAME=' + self.env_name + '\n' )
            f.close()
        else:
            print("There is no free environment available in the pool.")
            self.env_name = ''

    def get_env_array(self):
        if self.array == 'to_be_preloaded' :
            env_list = common.get_to_be_preloaded(self.data,self.release,self.version,
                                        self.type,self.pool,self.lease)
        if env_list :
            str_env_list = common.listToString(env_list)
            print("Pool of available environments:", env_list)
            f = open( '_array_env.txt', 'w' )
            f.write( str_env_list )
            f.close()
        else:
            print("There is no asking environment available in the pool.")

    def lease_env_item(self):
        data = common.lease_env(self.data,self.env_name,self.state,self.lease)
        with open( 'data.json', 'w' ) as outfile:
            json.dump(data, outfile)


def parse_args():
    """Parse command line arguments from sys.argv.
    Run script with--help to see the valid options.
    python3 yarn.py -f data.json -n <env_name>
    """
    desc = """Script performs command on server via ssh connection"""
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-f", "--file", default="data.json",
                        help="JSON file with data")
    parser.add_argument("-e", "--environment",
                        help="environment name")
    parser.add_argument("-s", "--state", default="preloaded",
                        help="preloaded, to_be_preloaded, not_loaded, tested, failed")
    parser.add_argument("-r", "--release", default="new_project",
                        help="release name")
    parser.add_argument("-v", "--version", default="0.1",
                        help="version")
    parser.add_argument("-t", "--type", default="vanilla",
                        help="ova, bin")
    parser.add_argument("-p", "--pool", default="dynamic", 
                        help="eng, pipeline")
    parser.add_argument("-l", "--lease", type=int, default=0,
                        help="ing, in seconds")
    parser.add_argument("-a", "--array",
                        help="get array of instances")
    return parser.parse_args()

if __name__ == '__main__':
    OPTIONS = parse_args()
    YARN = ActionYARN(OPTIONS)
    if not OPTIONS.environment:
        if OPTIONS.array:
            print("Get a list of the environment from the pool.")
            YARN.get_env_array()
        else:
            print("Get an environment from the pool.")
            YARN.get_env_item()
    else:
        print("Change a lease of the environment from the pool.")
        YARN.lease_env_item()
