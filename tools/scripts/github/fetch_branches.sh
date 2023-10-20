#!/bin/bash

ORG="Org"
OUTPUT_FILE="output.csv"

# Clear the output file or create it if it doesn't exist
> "$OUTPUT_FILE"

while read -r repo; do
    line="\"$repo\""  # Start the line with the repo name
    echo "Fetching branches for $repo..."
    branches=$(gh api repos/$ORG/$repo/branches | jq -r '.[].name')
    
    if [ -z "$branches" ]; then
        echo "Failed to retrieve branches for $repo. Skipping..."
    else
        for branch in $branches; do
            line+=",\"$branch\""
        done
        echo "$line" >> "$OUTPUT_FILE"  # Append the line to the CSV file
        echo "Branches for $repo retrieved successfully."
    fi
done < repos.txt

echo "Script completed."
