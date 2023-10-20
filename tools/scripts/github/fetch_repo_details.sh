#!/bin/bash

ORG="Org"
OUTPUT_FILE="output.csv"

# Clear the output file or create it if it doesn't exist
> "$OUTPUT_FILE"

while read -r repo; do
    line="\"$repo\""  # Start the line with the repo name
    echo "Fetching branches and additional information for $repo..."
    
    # Retrieve branches for the repository
    branches=$(gh api repos/$ORG/$repo/branches | jq -r '.[].name')
    
    # Retrieve additional information about the repository
    repo_info=$(gh api repos/$ORG/$repo | jq -r '[.default_branch, .branches_url, .language, .clone_url, .html_url] | @csv')

    if [ -z "$branches" ]; then
        echo "Failed to retrieve branches for $repo. Skipping..."
    else
        # Add additional repository information to the line
        line+=",$repo_info"
        # Add branches to the line
        for branch in $branches; do
            line+=",\"$branch\""
        done
        echo "$line" >> "$OUTPUT_FILE"  # Append the line to the CSV file
        echo "Data for $repo retrieved successfully."
    fi
done < repos.txt

echo "Script completed."
