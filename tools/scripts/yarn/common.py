#!/usr/bin/python3

import time


def listToString(s):
   # initialize an empty string
    str1 = " "
    # return string 
    return (str1.join(s))

def get_preloaded(data,arg_state,arg_release,arg_release_version,arg_type,arg_pool,arg_leased):
    """
    Get a preloaded VM from the list of VMs if VM meets the requirements 
    """
    arg_leased = int(arg_leased)
    env_list = []
    arg_lease_end_time = int(time.time())
    for i in data:
        res_state = data[i]['state']
        res_release = data[i]['release']
        res_release_version = data[i]['release_version']
        res_type = data[i]['type']
        res_pool = data[i]['pool']
        res_leased = data[i]['leased']
        res_lease_end_time = data[i]['lease_end_time']
        if res_leased != 0 :
            continue
        if res_state != arg_state :
            continue
        if res_release != arg_release :
            continue
        if res_release_version != arg_release_version :
            continue
        if res_type != arg_type :
            continue
        if res_pool != arg_pool :
            continue
        if res_leased != arg_leased :
            continue
        if res_lease_end_time > arg_lease_end_time :
            continue
        env_list.append(i)

    return env_list

def get_to_be_preloaded(data,arg_release,arg_release_version,arg_type,arg_pool,arg_leased):
    """
    Get a list of environment whish is not preloaded and stuck
    """
    arg_leased = int(arg_leased)
    env_list = []
    arg_lease_end_time = int(time.time())
    for i in data:
        res_state = data[i]['state']
        res_release = data[i]['release']
        res_release_version = data[i]['release_version']
        res_type = data[i]['type']
        res_pool = data[i]['pool']
        res_lease_end_time = data[i]['lease_end_time']
        if res_state == 'preloaded' :
            continue
        if res_lease_end_time > arg_lease_end_time :
            continue
        if res_release != arg_release :
            continue
        if res_release_version != arg_release_version :
            continue
        if res_type != arg_type :
            continue
        if res_pool != arg_pool :
            continue
        env_list.append(i)
    return env_list

def lease_env(data,env_name,state,lease):
    """
    Lease environment. Update state and lease end time.
    """
    current_time = int(time.time())
    lease = int(lease) #check lease is int

    if lease == 0 :
        lease = current_time
        leased = 0
    else :
        lease = current_time + lease
        leased = 1
    for i in data:
        if i == env_name:
            res_env = data[i]
            res_env["state"] = state
            res_env["lease_end_time"] = lease
            res_env["leased"] = leased
            data[env_name] = res_env
    return data
