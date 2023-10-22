#!/bin/bash
set +x && set -e

LIB_FILE="${WORKSPACE}/tools/lib/common.sh"
test -f ${LIB_FILE} && source ${LIB_FILE} || (echo "No common.sh" && exit 1)

get_vault

# If ENV_NAME is not defined choose ENV_NAME from the pool with state $1
echo "Getting pipeline environment from the yarn pool."
yarn_get_environment "$1" #state
source ./_env_name.txt
yarn_upadte_lease ${ENV_NAME} "to be preloaded" 3600
