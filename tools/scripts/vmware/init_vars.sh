#!/bin/bash
set -e
set +x

mkdir -p ${WORKSPACE}/target
LIB_FILE="${WORKSPACE}/tools/lib/common.sh"
test -f ${LIB_FILE} && source ${LIB_FILE} || (echo "No common.sh" && exit 1)

get_vault
# If ENV_NAME is not defined choose ENV_NAME from the pool
if [ -z ${ENV_NAME} ]; then
    echo "Getting pipeline environment from the yarn pool."
    yarn_get_environment "to be preloaded"
    export ENVIRONMENT_FROM_POOL=true
    source ./_env_name.txt
    yarn_upadte_lease ${ENV_NAME} "preloading" 10800
fi

# Get the kv secret from path
__keeper_get_secret "secret/dev/new_project/${ENV_NAME}"
echo $data | jq --arg env_name ${ENV_NAME} '. + {env_name: $env_name}' > ./vm_vars.json

# Get vars from default-new_project-vm-eng
__keeper_get_secret "secret/dev/new_project/default-new_project-vm-eng"
echo $data > ./default_vars.json

data=$(jq -s 'add' ./default_vars.json ./vm_vars.json)
echo $data > ./vm_init_vars.json
