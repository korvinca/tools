#!/bin/bash
set -e
set +x

function test {
    if [ -n "${SSH_CUSTOMER_PUBLIC_KEY}" ]; then
        echo "${SSH_CUSTOMER_PUBLIC_KEY}"
    else
        echo "Customer public key has not been provided."
    fi
}

test

SSH_CUSTOMER_PUBLIC_KEY=
test

SSH_CUSTOMER_PUBLIC_KEY=''
test

SSH_CUSTOMER_PUBLIC_KEY='key'
test