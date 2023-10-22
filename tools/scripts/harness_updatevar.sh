#!/bin/bash
set -ex

#TODO fetch those values from vault
apikey="${HARNESS_APIKEY}"
# identifier="sbtest1"
identifier=""
account="${HARNESS_ACCOUNT}"

project="ORGContinuousDeployment"
org="ORG"
# value="test-esaie-01"
value=""


usage() {
    cat <<EOF
$0: update variables in harness
   identifier:  harness variable identifier
   value:       harness variable new value
Common options:
  -i   identifier
  -v   value
Example:
   $0 -i "sbtest1" -v "test-esaie-01"
EOF
   exit 1
}

while getopts ":i:v:" o; do
    case "${o}" in
    i)
        identifier=${OPTARG}
        ;;
    v)
        value="${OPTARG}"
        ;;
    *)
        usage
        ;;
    esac
done
shift $((OPTIND - 1))

[ -z "${value}" ] && usage
[ -z "${identifier}" ] && usage

curl -X GET \
  "https://app.harness.io/gateway/ng/api/variables/$identifier?accountIdentifier=$account&orgIdentifier=$org&projectIdentifier=$project" \
  -H "x-api-key: $apikey" | tee g.json
  [ "$(jq -r '.status' g.json)" != "SUCCESS" ] && exit 1

vname=$(jq -r '.data.variable.name' g.json)
description=$(jq -r '.data.variable.description' g.json)
vtype=$(jq -r '.data.variable.type' g.json)
stype=$(jq -r '.data.variable.spec.valueType' g.json)

cat > payload.json <<EOF
{
  "variable": {
    "identifier": "$identifier",
    "name": "$vname",
    "description": "$description", 
    "orgIdentifier": "$org",
    "projectIdentifier": "$project",
    "type": "$vtype",
    "type": "String",
    "spec": {
      "valueType": "$stype",
      "fixedValue": "$value",
      "value": "$value"
    }
  }
}
EOF

curl -X PUT \
  "https://app.harness.io/gateway/ng/api/variables?accountIdentifier=$account" \
  -H 'Content-Type: application/json' \
  -H "x-api-key: $apikey" \
  -d @payload.json | tee g.json
[ "$(jq -r '.status' g.json)" != "SUCCESS" ] && exit 1

rm g.json payload.json
exit 0
