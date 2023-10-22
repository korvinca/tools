#!/bin/bash
set -e
set +x

LIB_FILE="${WORKSPACE}/tools/lib/common.sh"
test -f ${LIB_FILE} && source ${LIB_FILE} || exit 1
unset HTTP_PROXY && unset HTTPS_PROXY && unset http_proxy && unset https_proxy
print_log "Delete VM"
# TODO delete VM