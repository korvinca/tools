#!/usr/bin/env bash
set -x
. ./.gh-settings.conf

echo "----------------------------"
echo "Get all repos from ORG: $REPO_NAME"
echo "----------------------------"

repos_list=$(curl -L \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    $GITHUB_APIV3_BASE_URL/repos | jq -r '.[].name'
)

# TODO get repos from the github repository by pattern
# echo $repos_list > repos.list
