#!/bin/bash
set -e && set +x

LIB_FILE="${WORKSPACE}/tools/lib/common.sh"
test -f ${LIB_FILE} && source ${LIB_FILE} || (echo "No common.sh" && exit 1)

get_vault

# If ENV_NAME is not defined choose ENV_NAME from the pool
echo "Getting pipeline environment from the yarn pool."
yarn_upadte_lease $1 "to be preloaded" 0
