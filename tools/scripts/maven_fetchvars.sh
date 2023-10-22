#!/bin/bash
set -ex

# Generic method to retried k/v from maven
# by specifying the manifest, component and wanted keys
# this will extract values from given keys

manifest=""
component=""
keys=""
version=""
baseurl="https://maven.example.com/artifactory/symphony-group/com/example/vms/manifest"

usage() {
    cat <<EOF
$0: retrieves keys from the latest maven manifest zip archive
    creates a output.json file with the keys/values
maven url is in the format: base_url/manifest/component/
   baseurl:     maven base url
   manifest:    manifest folder
   component:   subcomponent name
   output:      output file name
Common options:
  -m   Manifest name
  -c   Component name
  -k   Key to retrieve from zip archive. multiple keys can be specified by repeating this options
  -o   Output filename (json)
Example:
   $0 -m "El-Stable" -c "infra-manifest" -k "consul_version" -k "vault_version" -o output.json
EOF
}

get_values() {
    maven_url="$baseurl/$manifest/$component/"
    curl $maven_url | grep -oP 'a href="\K([\d|\.|\-]+)' >a.log
    p=$(cat a.log | tail -1 | cut -d'-' -f1)
    s=$(grep -E "^$p-" a.log | cut -d'-' -f2 | sort -n | tail -1)
    version="$p-$s"

    mfile=$component-$version/infra_variables.yml
    curl -o r.zip $maven_url/$version/$component-$version-resources.zip
    rm $mfile || true
    unzip r.zip $mfile

    mjson="{}"
    for key in $keys; do
        value=""
        eval "value=\$(grep -oP \"^$key:\s+\K([\d|\.\-]+)\" $mfile)"
        echo "$mjson" | jq ". += { \"$key\": \"$value\" }" >output.json
        mjson=$(cat output.json)
    done
}

parse_args() {
    while getopts ":m:c:k:o:" o; do
        case "${o}" in
        m)
            manifest=${OPTARG}
            ;;
        c)
            component="${OPTARG}"
            ;;
        k)
            keys="$keys ${OPTARG}"
            ;;
        o)
            output="${OPTARG}"
            ;;
        *)
            usage
            ;;
        esac
    done
    shift $((OPTIND - 1))

    [ -z "${manifest}" ] && usage
    [ -z "${component}" ] && usage
    [ -z "${keys}" ] && usage
    [ -z "${output}" ] && usage

    echo "manifest: ${manifest}"
    echo "component: ${component}"
    echo "keys: ${keys}"
    echo "output: ${output}"
}

parse_args "$@"
get_values
cat output.json
