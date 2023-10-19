#!/usr/bin/env bash
set +x
. ./.gh-settings.conf
rm -rf tmp/repos-*

## Create Repo Folder w/Timestamp backup of the run
mkdir -p tmp/repos-"$SERIAL_NUMBER"

# Main Branch Prep
graphql_query_m=tmp/repos-"$SERIAL_NUMBER"/graphql_query_m.txt
rm -f ${graphql_query_m}
json_file_m=tmp/repos-"$SERIAL_NUMBER"/graphql-payload_m.json
rm -f ${json_file_m}

# Release Branch Prep
graphql_query_r=tmp/repos-"$SERIAL_NUMBER"/graphql_query_r.txt
rm -f ${graphql_query_r}
json_file_r=tmp/repos-"$SERIAL_NUMBER"/graphql-payload_r.json
rm -f ${json_file_r}

# Develop Branch Prep
graphql_query_d=tmp/repos-"$SERIAL_NUMBER"/graphql_query_d.txt
rm -f ${graphql_query_d}
json_file_d=tmp/repos-"$SERIAL_NUMBER"/graphql-payload_d.json
rm -f ${json_file_d}

# Feature Branch Prep
graphql_query_f=tmp/repos-"$SERIAL_NUMBER"/graphql_query_f.txt
rm -f ${graphql_query_f}
json_file_f=tmp/repos-"$SERIAL_NUMBER"/graphql-payload_f.json
rm -f ${json_file_f}

# Hotfix Branch Prep
graphql_query_h=tmp/repos-"$SERIAL_NUMBER"/graphql_query_h.txt
rm -f ${graphql_query_f}
json_file_h=tmp/repos-"$SERIAL_NUMBER"/graphql-payload_h.json
rm -f ${json_file_h}

# Bugfix Branch Prep
graphql_query_b=tmp/repos-"$SERIAL_NUMBER"/graphql_query_b.txt
rm -f ${graphql_query_f}
json_file_b=tmp/repos-"$SERIAL_NUMBER"/graphql-payload_b.json
rm -f ${json_file_b}

# Wildcard Branch Prep
graphql_query_w=tmp/repos-"$SERIAL_NUMBER"/graphql_query_w.txt
rm -f ${graphql_query_w}
json_file_w=tmp/repos-"$SERIAL_NUMBER"/graphql-payload_w.json
rm -f ${json_file_w}

main() {
    cat <<EOF >$graphql_query_m
    mutation {
        createBranchProtectionRule(
            input: {
                repositoryId:$repository_id,
                pattern:"$pattern",
                requiresApprovingReviews: true
                requiredApprovingReviewCount: 2
                allowsDeletions: false
                allowsForcePushes: false
                blocksCreations: false
                dismissesStaleReviews: true
                isAdminEnforced: true
                requiresCodeOwnerReviews: false
                requiresCommitSignatures: false
                requiresLinearHistory: false
                requiresStatusChecks: false
                requiredStatusCheckContexts: []
                requiresStrictStatusChecks: false
                restrictsPushes: false
                requireLastPushApproval: false
                restrictsReviewDismissals: false
                requiresConversationResolution: false
                }
            ) {
            clientMutationId
        }
    }
EOF

    jq -n \
        --arg graphql_query "$(cat $graphql_query_m)" \
        '{query: $graphql_query}' >${json_file_m}

    curl ${curl_custom_flags} \
        -H "Accept: application/vnd.github.v3+json" \
        -H 'Accept: application/vnd.github.audit-log-preview+json' \
        -H "Authorization: Bearer ${GITHUB_TOKEN}" \
        ${GITHUB_APIV4_BASE_URL} -d @${json_file_m}
}

release() {
    cat <<EOF >$graphql_query_r
    mutation {
        createBranchProtectionRule(
            input: {
                repositoryId:$repository_id,
                pattern:"$pattern",
                requiresApprovingReviews: true
                requiredApprovingReviewCount: 2
                allowsDeletions: false
                allowsForcePushes: false
                blocksCreations: false
                dismissesStaleReviews: true
                isAdminEnforced: true
                requiresCodeOwnerReviews: false
                requiresCommitSignatures: false
                requiresLinearHistory: false
                requiresStatusChecks: false
                requiredStatusCheckContexts: []
                requiresStrictStatusChecks: false
                restrictsPushes: false
                requireLastPushApproval: false
                restrictsReviewDismissals: false
                requiresConversationResolution: false
                }
            ) {
            clientMutationId
        }
    }
EOF

    jq -n \
        --arg graphql_query "$(cat $graphql_query_r)" \
        '{query: $graphql_query}' >${json_file_r}

    curl ${curl_custom_flags} \
        -H "Accept: application/vnd.github.v3+json" \
        -H 'Accept: application/vnd.github.audit-log-preview+json' \
        -H "Authorization: Bearer ${GITHUB_TOKEN}" \
        ${GITHUB_APIV4_BASE_URL} -d @${json_file_r}
}

develop() {
    cat <<EOF >$graphql_query_d
    mutation {
        createBranchProtectionRule(
            input: {
                repositoryId:$repository_id,
                pattern:"$pattern",
                requiresApprovingReviews: true
                requiredApprovingReviewCount: 1
                allowsDeletions: false
                allowsForcePushes: false
                blocksCreations: false
                dismissesStaleReviews: true
                isAdminEnforced: true
                requiresCodeOwnerReviews: false
                requiresCommitSignatures: false
                requiresLinearHistory: false
                requiresStatusChecks: false
                requiredStatusCheckContexts: []
                requiresStrictStatusChecks: false
                restrictsPushes: false
                requireLastPushApproval: false
                restrictsReviewDismissals: false
                requiresConversationResolution: false
                }
            ) {
            clientMutationId
        }
    }
EOF

    jq -n \
        --arg graphql_query "$(cat $graphql_query_d)" \
        '{query: $graphql_query}' >${json_file_d}

    curl ${curl_custom_flags} \
        -H "Accept: application/vnd.github.v3+json" \
        -H 'Accept: application/vnd.github.audit-log-preview+json' \
        -H "Authorization: Bearer ${GITHUB_TOKEN}" \
        ${GITHUB_APIV4_BASE_URL} -d @${json_file_d}
}

feature() {
    cat <<EOF >$graphql_query_f
    mutation {
        createBranchProtectionRule(
            input: {
                repositoryId:$repository_id,
                pattern:"$pattern",
                requiresApprovingReviews: false
                requiredApprovingReviewCount: null
                allowsDeletions: true
                allowsForcePushes: true
                blocksCreations: false
                dismissesStaleReviews: false
                isAdminEnforced: false
                requiresCodeOwnerReviews: false
                requiresCommitSignatures: false
                requiresLinearHistory: false
                requiresStatusChecks: false
                requiredStatusCheckContexts: []
                requiresStrictStatusChecks: true
                restrictsPushes: false
                requireLastPushApproval: false
                restrictsReviewDismissals: false
                requiresConversationResolution: false
                }
            ) {
            clientMutationId
        }
    }
EOF

    jq -n \
        --arg graphql_query "$(cat $graphql_query_f)" \
        '{query: $graphql_query}' >${json_file_f}

    curl ${curl_custom_flags} \
        -H "Accept: application/vnd.github.v3+json" \
        -H 'Accept: application/vnd.github.audit-log-preview+json' \
        -H "Authorization: Bearer ${GITHUB_TOKEN}" \
        ${GITHUB_APIV4_BASE_URL} -d @${json_file_f}
}

bugfix() {
    cat <<EOF >$graphql_query_b
    mutation {
        createBranchProtectionRule(
            input: {
                repositoryId:$repository_id,
                pattern:"$pattern",
                requiresApprovingReviews: false
                requiredApprovingReviewCount: null
                allowsDeletions: true
                allowsForcePushes: true
                blocksCreations: false
                dismissesStaleReviews: false
                isAdminEnforced: false
                requiresCodeOwnerReviews: false
                requiresCommitSignatures: false
                requiresLinearHistory: false
                requiresStatusChecks: false
                requiredStatusCheckContexts: []
                requiresStrictStatusChecks: true
                restrictsPushes: false
                requireLastPushApproval: false
                restrictsReviewDismissals: false
                requiresConversationResolution: false
                }
            ) {
            clientMutationId
        }
    }
EOF

    jq -n \
        --arg graphql_query "$(cat $graphql_query_b)" \
        '{query: $graphql_query}' >${json_file_b}

    curl ${curl_custom_flags} \
        -H "Accept: application/vnd.github.v3+json" \
        -H 'Accept: application/vnd.github.audit-log-preview+json' \
        -H "Authorization: Bearer ${GITHUB_TOKEN}" \
        ${GITHUB_APIV4_BASE_URL} -d @${json_file_b}
}

hotfix() {
    cat <<EOF >$graphql_query_h
    mutation {
        createBranchProtectionRule(
            input: {
                repositoryId:$repository_id,
                pattern:"$pattern",
                requiresApprovingReviews: false
                requiredApprovingReviewCount: null
                allowsDeletions: true
                allowsForcePushes: true
                blocksCreations: false
                dismissesStaleReviews: false
                isAdminEnforced: false
                requiresCodeOwnerReviews: false
                requiresCommitSignatures: false
                requiresLinearHistory: false
                requiresStatusChecks: false
                requiredStatusCheckContexts: []
                requiresStrictStatusChecks: true
                restrictsPushes: false
                requireLastPushApproval: false
                restrictsReviewDismissals: false
                requiresConversationResolution: false
                }
            ) {
            clientMutationId
        }
    }
EOF

    jq -n \
        --arg graphql_query "$(cat $graphql_query_h)" \
        '{query: $graphql_query}' >${json_file_h}

    curl ${curl_custom_flags} \
        -H "Accept: application/vnd.github.v3+json" \
        -H 'Accept: application/vnd.github.audit-log-preview+json' \
        -H "Authorization: Bearer ${GITHUB_TOKEN}" \
        ${GITHUB_APIV4_BASE_URL} -d @${json_file_h}
}

wildcard() {
    cat <<EOF >$graphql_query_w
    mutation {
        createBranchProtectionRule(
            input: {
                repositoryId:$repository_id,
                pattern:"$pattern",
                requiresApprovingReviews: false
                requiredApprovingReviewCount: null
                allowsDeletions: false
                allowsForcePushes: false
                blocksCreations: true
                dismissesStaleReviews: false
                isAdminEnforced: true
                requiresCodeOwnerReviews: false
                requiresCommitSignatures: false
                requiresLinearHistory: false
                requiresStatusChecks: false
                requiredStatusCheckContexts: []
                requiresStrictStatusChecks: true
                restrictsPushes: true
                restrictsReviewDismissals: false
                requiresConversationResolution: false
                }
            ) {
            clientMutationId
        }
    }
EOF

    jq -n \
        --arg graphql_query "$(cat $graphql_query_w)" \
        '{query: $graphql_query}' >${json_file_w}

    curl ${curl_custom_flags} \
        -H "Accept: application/vnd.github.v3+json" \
        -H 'Accept: application/vnd.github.audit-log-preview+json' \
        -H "Authorization: Bearer ${GITHUB_TOKEN}" \
        ${GITHUB_APIV4_BASE_URL} -d @${json_file_w}
}

## Update Repo
while IFS= read -r REPO_NAME || [[ -n "$REPO_NAME" ]]; do
    echo "----------------------------"
    echo "REPO: $REPO_NAME"
    echo "Admin Access: $ADMIN_TEAM"
    echo "Dev Access: $DEV_TEAM"
    echo "----------------------------"
    echo "Update Repo $REPO_NAME"
    repo_id=$(curl -L \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer $GITHUB_TOKEN" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        $GITHUB_API_BASE_URL/repos/$GITHUB_ORG/$REPO_NAME | jq -r '.id')

    echo "Update $REPO_NAME:$repo_id"

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

    ## Getting Repo Node ID
    read -r -d '' graphql_script <<EOF
    { repository(owner: "$GITHUB_ORG", name: "$REPO_NAME") {id} } 
EOF

    graphql_script="$(echo ${graphql_script//\"/\\\"})"
    repository_id=$(curl -L \
        -H "Accept: application/vnd.github.v3+json" \
        -H 'Accept: application/vnd.github.audit-log-preview+json' \
        -H "Authorization: Bearer ${GITHUB_TOKEN}" \
        ${GITHUB_APIV4_BASE_URL} -d "{ \"query\": \"$graphql_script\"}" | jq .[].repository.id)

    ## Create Branch protection rules
    pattern="main"
    echo "Creating Branch Protection Rule: $pattern"
    main
    pattern="release"
    echo "Creating Branch Protection Rule: $pattern"
    release
    pattern="develop"
    echo "Creating Branch Protection Rule: $pattern"
    develop
    pattern="feature/*"
    echo "Creating Branch Protection Rule: $pattern"
    feature
    pattern="hotfix/*"
    echo "Creating Branch Protection Rule: $pattern"
    hotfix
    pattern="bugfix/*"
    echo "Creating Branch Protection Rule: $pattern"
    bugfix
    pattern="*"
    echo "Creating Branch Protection Rule: $pattern"
    wildcard

    ## Setting Default Branch
    echo "Update default branch to $DEFAULT_BRANCH"
    default_output=$(curl -L \
        -X PATCH \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer $GITHUB_TOKEN" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        $GITHUB_API_BASE_URL/repos/$GITHUB_ORG/$REPO_NAME \
        -d "{\"default_branch\":\"$DEFAULT_BRANCH\"}"
    )

done < "repos.list"
