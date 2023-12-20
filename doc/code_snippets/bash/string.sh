# github_url = "https://api.github.com/repos/docker/compose/releases"
# Visit the URL above, parse received data, and display all release versions referenced by the key "tag_name".

#curl -o data.json https://api.github.com/repos/docker/compose/releases
#cat data.json | grep "tag_name" | cut -d ":" -f2 | cut -d "\"" -f2 | wc -l

# Declare a variable
name="John Doe"

# Extract the substring "John"
firstName=$(echo ${name} | cut -d ' ' -f 1)

# Print the substring "John"
echo "First name is: $firstName"

# Extract the substring "Doe"
lastName=$(echo ${name} | cut -d ' ' -f 2)

# Print the substring "Doe"
echo "Last name is: $lastName"