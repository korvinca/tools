# README


## Objective
Sync variables between maven manifest and harness inputsets in a pipeline

## Pre-requisites
- pipeline in harness where variables are defined
- inputset must be defined with the config variables
 variable type is `string`

## Files
- maven-harness-vars.py: python script to sync variables between maven and harness inputsets or a pipeline
- config.yml: parameters used by the python script
- Jenkinsfile: Jenkins pipeline
- requirements.txt: python3 python import modules

## Usage
```bash
export VAULT_TOKEN=***
./maven-harness-vars.py \
  --config "config.yml" \
  --version "latest"
```
