#!/bin/bash
set -e
set +x

LIB_FILE="${WORKSPACE}/tools/lib/common.sh"
test -f ${LIB_FILE} && source ${LIB_FILE} || exit 1

# Check if a JSON file is provided as a parameter
if [ -z "$1" ]; then
    print_error "Please provide a JSON file as a parameter."
fi

# Run the function with the JSON file parameter
export_json_to_env "$1"
