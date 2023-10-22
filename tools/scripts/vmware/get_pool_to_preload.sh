#!/bin/bash
set +x && set -e
LIB_FILE="${WORKSPACE}/tools/lib/common.sh"
test -f ${LIB_FILE} && source ${LIB_FILE} || (echo "No common.sh" && exit 1)

get_vault

yarn_get_environment_from_pool_to_preload

if [ -f ${WORKSPACE}/_array_env.txt ] ; then
   arraEnv=( $( cat ${WORKSPACE}/_array_env.txt ) )
   for i in "${arrayEnv[@]}"
   do
      print_log "Change status to be preload: $i"
      yarn_upadte_lease $i "to be preloaded" 0
   done
else
   print_log "No environment to be preload."
fi