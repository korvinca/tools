#!/usr/bin/env bash
set +x
. ./.gh-settings.conf

## Create Repo
while IFS= read -r REPO_NAME || [[ -n "$REPO_NAME" ]]; do
    echo "----------------------------"
    echo "REPO: $REPO_NAME"
    echo "Admin Access: $ADMIN_TEAM"
    echo "Dev Access: $DEV_TEAM"
    echo "----------------------------"
    
    echo "Check if repo exists: $REPO_NAME"
    repo_id=$(curl -L \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer $GITHUB_TOKEN" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        $GITHUB_API_BASE_URL/repos/$GITHUB_ORG/$REPO_NAME | jq -r '.id')

    if [[ "$repo_id" == null ]] ; then
        echo "Create Repo $REPO_NAME"
        new_repo=$(curl -L \
            -X POST \
            -H "Accept: application/vnd.github+json" \
            -H "Authorization: Bearer $GITHUB_TOKEN" \
            -H "X-GitHub-Api-Version: 2022-11-28" \
            $GITHUB_API_BASE_URL/repos/$GITHUB_ORG/$TEMPLATE_REPO_NAME/generate \
            --data-binary @- <<EOF
            {"owner":"$GITHUB_ORG","name":"$REPO_NAME","description":"$REPO_NAME","include_all_branches":true,"private":true}
EOF
        )
        repo_id=$(echo $new_repo | jq -r '.id')
        echo "Created $REPO_NAME:$repo_id"
        echo "Wait 5 seconds & continue..."
        sleep 5
    else
        echo "Repo $REPO_NAME exists. Nothing to do."
        continue
    fi

    ## Add Development Branch
    echo "Creating Development Branch for $REPO_NAME"

    ## Get Develop Branch Information
    echo "Getting Repo $REPO_NAME main branch information"
    SHA=$(curl -L \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer $GITHUB_TOKEN" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        https://api.github.com/repos/$GITHUB_ORG/$REPO_NAME/git/refs/heads/main | jq -r '.object.sha')

    curl ${curl_custom_flags} \
        -X POST \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer $GITHUB_TOKEN" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        -d  "{\"ref\": \"refs/heads/development\",\"sha\": \"$SHA\"}" \
        https://api.github.com/repos/$GITHUB_ORG/$REPO_NAME/git/refs

    ## Add team access to repo: w/ADMIN
    if [[ -n "$ADMIN_TEAM" ]] ; then
        echo "Adding $ADMIN_TEAM to $REPO_NAME with [ADMIN] access"
        curl ${curl_custom_flags} \
            -X PUT \
            -H "Accept: application/vnd.github+json" \
            -H "Authorization: Bearer $GITHUB_TOKEN" \
            -H "X-GitHub-Api-Version: 2022-11-28" \
            $GITHUB_APIV3_BASE_URL/teams/$ADMIN_TEAM/repos/$GITHUB_ORG/$REPO_NAME \
            -d '{"permission":"admin"}'
    fi

    ## Add team access to repo: w/PUSH (WRITE)
    if [[ -n "$DEV_TEAM" ]] ; then
        echo "Adding $DEV_TEAM to $REPO_NAME with [PUSH] (WRITE) access"
        curl ${curl_custom_flags} \
            -X PUT \
            -H "Accept: application/vnd.github+json" \
            -H "Authorization: Bearer $GITHUB_TOKEN" \
            -H "X-GitHub-Api-Version: 2022-11-28" \
            $GITHUB_APIV3_BASE_URL/teams/$DEV_TEAM/repos/$GITHUB_ORG/$REPO_NAME \
            -d '{"permission":"push"}'
    fi

done < "repos.list"