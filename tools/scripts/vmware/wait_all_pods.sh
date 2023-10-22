#!/bin/bash
set -e
set +x

function __is_deployment_ready() {

  period="$1"
  interval="$2"
  
  for ((i=0; i<$period; i+=$interval)); do
    if ! command -v kubectl &> /dev/null
    then
      echo "kubectl could not be found, waiting..."
      sleep "$interval"
      continue
    fi
    if kubectl get deployment -n starship-devops | grep -q 'kibana' ; then
      echo "deployment kibana found."
      kubectl rollout status deployment/kibana -n starship-devops || exit 1
      return 0
    else
      echo "deployment kibana could not be found, waiting..."
      sleep "$interval"
    fi
  done
}

function __is_pod_ready() {
  [[ "$(kubectl get po "$1" -n default -o 'jsonpath={.status.conditions[?(@.type=="Ready")].status}')" == 'True' ]]
}

function __pods_ready() {
  local pod

  [[ "$#" == 0 ]] && return 0

  for pod in $pods; do
    __is_pod_ready "$pod" || return 1
  done

  return 0
}

function __wait-until-pods-ready() {
  local period interval i pods

  if [[ $# != 2 ]]; then
    echo "Usage: wait-until-pods-ready PERIOD INTERVAL" >&2
    echo "" >&2
    echo "This script waits for all pods to be ready in the current namespace." >&2

    return 1
  fi

  period="$1"
  interval="$2"

  for ((i=0; i<$period; i+=$interval)); do
    pods="$(kubectl get po -n default -o 'jsonpath={.items[*].metadata.name}')"
    if __pods_ready $pods; then
      touch /tmp/bin_ready.txt
      return 0
    fi

    echo "Waiting for pods to be ready..."
    sleep "$interval"
  done

  echo "Waited for $period seconds, but all pods are not ready yet."
  return 1
}

__is_deployment_ready $@
__wait-until-pods-ready $@
# vim: ft=sh :
# ./test.sh 3600 60