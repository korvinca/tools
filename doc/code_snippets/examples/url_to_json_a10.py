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
