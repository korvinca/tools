#!/bin/bash
set -e
set +x

LIB_FILE="${WORKSPACE}/tools/lib/common.sh"
test -f "${LIB_FILE}" && source "${LIB_FILE}" || (echo "no common.sh" && exit 1)
test -f ./_env_name.txt && source ./_env_name.txt || print_log "No _env_name.txt file. The ENV_NAME is predefined."

# Update lease
yarn_upadte_lease ${ENV_NAME} "preloading" 10800 || true

print_log "Install ofvtool"
install_ovftool

print_log "Install govc"
install_govc

print_log "Set vars"
export_json_to_env "./vm_init_vars.json"
test -f ./vm_init_vars.env && source ./vm_init_vars.env || exit 1
OVA_URL_NAS="${source_nas}${OVA_FILE}"
OVA_URL_ARTIFACTORY="${source_artifactory}${OVA_FILE}"
IMAGE_URL_NAS="${source_nas}${BINARY_FILE}"
IMAGE_URL_ARTIFACTORY="${source_artifactory}${BINARY_FILE}"
VM_NAME="${env_name}.${dns_search_domain}"
PRIV_KEY_FILE="${WORKSPACE}/vm_ssh_private_key"
ANSIBLE_USER="ansible"
ANSIBLE_PASS="${user_password}"
IMAGE_FOLDER="/example/upload"
SSH_TARGET="-i ${PRIV_KEY_FILE} ${ANSIBLE_USER}@${VM_NAME}"

sudo rm -rf "${PRIV_KEY_FILE}"
echo "${vm_ssh_private_key}" > "${PRIV_KEY_FILE}"
chmod 400 "${PRIV_KEY_FILE}"

print_log "Configure govc environment"
export GOVC_URL="${vcenter_url}"
export GOVC_USERNAME="${vcenter_username}"
export GOVC_PASSWORD="${vcenter_password}"

function check_host() {
    print_log "Waiting for host to be ready"
    sleep 120 #for failed/running pods
    waiting_for_host_ssh 300 10 ${PRIV_KEY_FILE} ${ANSIBLE_USER}@${VM_NAME}
    ssh -q ${SSH_TARGET} "bash -c 'bash /tmp/wait_all_pods.sh 1200 30'"
    print_log "Applince is ready. All pods are up and running."
}

function ova_deployment() {
    print_log "================================= OVA deployment ====================================================="
    select_source "${OVA_URL_NAS}" "${OVA_URL_ARTIFACTORY}" && OVA_URL="${SELECTED_URL}"
    ovftool --deploymentOption=small \
    --X:logLevel=verbose \
    --X:logFile=ovftool-log.txt \
    --allowExtraConfig \
    --noSSLVerify \
    --diskMode=thin \
    --acceptAllEulas \
    --skipManifestCheck \
    --powerOn \
    --vmFolder="${vm_folder}" \
    --datastore="${datastore}" \
    --overwrite="true" \
    --powerOffTarget \
    --name="${VM_NAME}" \
    --network="${network}" \
    --prop:ssh-authorized-keys="${vm_ssh_public_key}" \
    --prop:ntp-servers="${ntp_server}" \
    --prop:password="${user_password}" \
    --prop:dns-search-domain="${dns_search_domain}" \
    --prop:ipv4-addr="${ipv4_address}" \
    --prop:ipv4-dns-servers="${ipv4_dns_servers}" \
    --prop:ipv4-gateway="${ipv4_gateway}" \
    --prop:ipv4-mask="${ipv4_mask}" \
    --prop:enable-dhcp="False" \
    --prop:cloud="False" \
    --prop:cloud-host="stagingconnect.starshipcloud.com" \
    --prop:disable-dev-env="False" \
    --prop:skip-debug="False" \
    --prop:skip-init="False" \
    "${OVA_URL}" \
    "vi://${vcenter_username}:${vcenter_password}@${vcenter_url}/${dc}/host/${cluster}" 2>&1

    print_log "Waiting for portal to be ready"
    waiting_for_portal "${VM_NAME}"

    print_log "================================= Post deployment config ====================================================="

    print_log "Add SSH_CUSTOMER_PUBLIC_KEY if it is not empty"
    if [ -n "${SSH_CUSTOMER_PUBLIC_KEY}" ]; then
        inject_public_key
    else
        print_log "Customer public key has not been provided."
    fi

    # Enable ssh localhost password auth
    ssh ${SSH_TARGET} "sudo bash -c 'cat >> /etc/ssh/sshd_config'" << EOF
    Match Address 127.0.0.0/8
     PasswordAuthentication yes
EOF
    ssh ${SSH_TARGET} "sudo systemctl restart sshd"
    # Set ansible user password
    ssh ${SSH_TARGET} "echo '${ANSIBLE_USER}:${ANSIBLE_PASS}' | sudo chpasswd"
}

function binary_deployment() {
    print_log "================================= Binary deployment ====================================================="

    select_source "${IMAGE_URL_NAS}" "${IMAGE_URL_ARTIFACTORY}" && IMAGE_URL="${SELECTED_URL}"
    
    print_log "Download Binary image"
    ssh ${SSH_TARGET} "cd ${IMAGE_FOLDER} && curl -LO '${IMAGE_URL}'"

    print_log "Set appliance deployment cap"
    curl -k -X POST https://${VM_NAME}/connector/SetupInfo -d@- << EOF
    {"Capabilities":[{"Key":"example.meta.appliance.intersightappliance"}],"DeploymentMode":"Private"}
EOF

    print_log "Activate downloader"
    curl -k -X PATCH https://${VM_NAME}/connector/SetupInfo -d@- << EOF
    {
     "SetupStates": ["download"]
    }
EOF

    ## TODO: /connector/HttpProxies
    print_log "Provide download details"
    curl -k -X POST https://${VM_NAME}/connector/RemoteFileImport -d@- << EOF
    {
     "Protocol":"scp",
     "RemoteHost":"127.0.0.1",
     "RemotePort":22,
     "RemotePath":"${IMAGE_FOLDER}",
     "Filename":"${BINARY_FILE}",
     "Username":"${ANSIBLE_USER}",
     "Password":"${ANSIBLE_PASS}"
    }
EOF

    print_log "Waiting for Binary installation to complete."
    print_log "Waiting 2 hours before check Binary."

    sleep 6000

    print_log "Check Binary installation is complete. Period 1 hour."
    waiting_for_portal "${VM_NAME}"
    scp -i ${PRIV_KEY_FILE} ${WORKSPACE}/tools/scripts/vmware/wait_all_pods.sh ${ANSIBLE_USER}@${VM_NAME}:/tmp/wait_all_pods.sh
    ## TODO: Run script on slave
    ssh -q ${SSH_TARGET} "bash -c 'bash /tmp/wait_all_pods.sh 3600 60'"
    print_log "Applince is ready. All pods are up and running."
    #TODO 
    sleep 300
    print_log "Take Binary snapshot after binary deployment"
    if [ "${CREATE_SNAP}" = true ] ; then
        print_log "Create snapshot of Binary"
        create_snapshot "${VM_NAME}" "${BINARY_FILE}" "Cold"
        check_host
    fi
}

print_log "Check Binary snapshots exist"
binary_snap=$(govc snapshot.tree -k -vm "${VM_NAME}" | grep "${BINARY_FILE}" | awk '{ gsub(/ /, ""); print }')

if [ -n "${binary_snap}" ] && [ "${binary_snap}" == "${BINARY_FILE}" ]; then
    print_log "Snapshot of Binary found"
    revert_snapshot "${VM_NAME}" "${BINARY_FILE}" "Cold"
    sleep 180
    waiting_for_host_ssh 300 10 ${PRIV_KEY_FILE} ${ANSIBLE_USER}@${VM_NAME}
    print_log "Add SSH_CUSTOMER_PUBLIC_KEY if it is not empty"
    if [ -n "${SSH_CUSTOMER_PUBLIC_KEY}" ]; then
        inject_public_key
    else
        print_log "Customer public key has not been provided."
    fi
    check_host
else
    print_log "Snapshot of Snapshot of Binary dosn't meet required Binary version. Rebuildnig VM."
    ova_deployment
    if [ "${DEPLOY_BIN}" = true ] ; then
        print_log "Deploy Binary"
        binary_deployment
    fi
fi

# Update lease
yarn_upadte_lease ${ENV_NAME} "preloaded" 0  || true
