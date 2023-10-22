# github_url = "https://api.github.com/repos/docker/compose/releases"
# Visit the URL above, parse received data, and display all release versions referenced by the key "tag_name".

# curl -o data.json https://api.github.com/repos/docker/compose/releases
# cat data.json | grep "tag_name" | cut -d ":" -f2 | cut -d "\"" -f2 | wc -l

import urllib.request
import json

with urllib.request.urlopen('https://api.github.com/repos/docker/compose/releases') as response:
    html = response.read()
    data = json.loads(html)
    # count = 0
    for i in data :
        print(i['tag_name'])
        # print(data[count]['tag_name'])
        # count = count + 1 
