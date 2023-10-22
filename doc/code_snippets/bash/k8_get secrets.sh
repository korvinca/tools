#!/bin/bash
set -e
mkdir -p /tmp/secrets
rm -rf /tmp/secrets/* /tmp/secrets.tgz /tmp/secret_name.txt
kubectl get secrets > /tmp/secret_name.txt
cat /tmp/secret_name.txt | while read line
do
    s_name=$(echo $line | head -n1 | cut -d " " -f1)
    echo $s_name
    if [ $s_name == 'NAME' ] ; then
        continue
    fi
    kubectl get secret $s_name -o yaml > /tmp/secrets/secret_$s_name.yaml
    #kubectl get secret $s_name -o json > /tmp/secrets/secret_$s_name.json
done
tar -czf /tmp/secrets.tgz /tmp/secrets
rm -rf /tmp/secrets /tmp/secrets.tgz /tmp/secret_name.txt