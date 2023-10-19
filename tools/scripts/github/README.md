# GitHub Repo Automation and Documentation

This folder contains all the code needed to create and manage repos, branches, and security settings for GitHub external repos.  This project exists to not only create new repositories in the various GitHub Organizations, but also to help secure and lock down the existing repositories used for the pipeline.

In order for us to adheer to the requirements laid out before us and ensure the enforment of the policies we are implementing the following changes:

* Organization Ownership rights will be to a limited group of people
* The number of users with Admin Access to repos will be limited and controlled
* Branch Protection rules will be implemented
* Requirement of 1 reviewer PRs
* Disallowing force merges in PRs

In this README, we will take the time to walk you through the current configuration and changes we will make to repos with the automation scripts

## GitHub Organizations Supported

```bash
My-Org
```

## Automation

```bash
#Create a file .gh-settings.conf in tools/scripts/github before run scripts:
#ORG sensitive variables. Add them first
GITHUB_TOKEN="<github_token>"

#GitHub Variables for the URL, hostname, and prefix for curl command
GITHUB_ORG="My-Org"
GITHUB_API_BASE_URL="https://api.github.com"
GITHUB_APIV3_BASE_URL="${GITHUB_API_BASE_URL}/orgs/${GITHUB_ORG}"
GITHUB_APIV4_BASE_URL="${GITHUB_API_BASE_URL}/graphql"
DEV_TEAM="Devs"
ADMIN_TEAM="Admins"
#Precreate template repo with main branch as default
TEMPLATE_REPO_NAME="DevOps.Template"
DEFAULT_BRANCH="main"

#Some Variables
SERIAL_NUMBER=$(date '+%m%d%Y-%H%M%S')
curl_custom_flags="-s -L"
```

### Scripts

```ruby
tools/
└── src/
    └── tools/
        └── scripts/
            └── github/
                ├── .gh-settings.conf
                ├── create_repos.sh
                ├── get_repos_list.sh
                ├── README.md
                ├── repos.list
                ├── update_repos.sh
```

In the above file diagram, we omitted folders and files to highlight the files referenced in this documentation section.

### To create repo(s)
* cretae file tools/scripts/github/.gh-settings.conf with corretc Github token
* add repo name to the repos.list file. One repo name per line 
* run script to create repos from the repos.list using template from .gh-settings.conf
```bash
cd tools/scripts/github
./create_repos.sh
```

### To update repo(s)
* cretae file tools/scripts/github/.gh-settings.conf with corretc Github token
* add repo name to the repos.list file. One repo name per line 
* run script to update repos from the repos.list
```bash
cd tools/scripts/github
./update_repos.sh
```
