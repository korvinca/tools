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
    yarn_get_environment "preloaded"
    export ENVIRONMENT_FROM_POOL=true
    source ./_env_name.txt
fi

__keeper_get_secret "secret/dev/new_project/${ENV_NAME}"
echo $data | jq --arg env_name ${ENV_NAME} '. + {env_name: $env_name}' > ./vm_vars.json

__keeper_get_secret "secret/dev/new_project/default-new_project-vm-eng"
echo $data > ./default_vars.json

__keeper_get_secret "secret/dev/new_project/harness_sandbox"
echo "$(jq -r '.["vars"]' <<<$data)" >> ./tools/ansible/roles/harness-init/defaults/main.yml

data=$(jq -s 'add' ./default_vars.json ./vm_vars.json)
echo $data > ./vm_init_vars.json

export_json_to_env "./vm_init_vars.json"
test -f ./vm_init_vars.env && source ./vm_init_vars.env || exit 1

PRIV_KEY_FILE="${WORKSPACE}/appliance.pem"
rm -rf "${PRIV_KEY_FILE}"
echo "${vm_ssh_private_key}" > "${PRIV_KEY_FILE}" && chmod 400 "${PRIV_KEY_FILE}"
echo "env_name: \"${ENV_NAME}\"" >> tools/ansible/group_vars/all/main.yml
echo "[appliances]" >> tools/ansible/inventory
echo "appliance ansible_host="${ipv4_address}" ansible_user=ansible ansible_ssh_private_key_file=$PRIV_KEY_FILE ansible_python_interpreter=/usr/bin/python3" >> tools/ansible/inventory

# cp ./vm_init_vars.env "${WORKSPACE}/target/vm_init_vars.env"
# cp tools/ansible/inventory ${WORKSPACE}/target/
# cp $PRIV_KEY_FILE ${WORKSPACE}/target/
cp tools/ansible/group_vars/all/main.yml ${WORKSPACE}/target/
