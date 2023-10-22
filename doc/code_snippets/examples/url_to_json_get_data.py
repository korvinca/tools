import urllib.request
import json

def parcing_url(url):
    response = urllib.request.urlopen(url)
    body = response.read().decode("utf-8")
    # file = open("data.json","w")
    # file.write(body)
    # # f = open("data.json", "r")
    # # new_data = json.loads(f.read())
    data = json.loads(body)
    print(data)
    print(f"gender: {data['results'][0]['gender']}")
    print(f"name: {data['results'][0]['name']['first']} {data['results'][0]['name']['last']}")
    print(f"country: {data['results'][0]['location']['country']}")

def parcing_url_aws(url):
    response = urllib.request.urlopen(url)
    body = response.read().decode("utf-8")
    data = json.loads(body)
    # print(data['prefixes'])
    for prefix in data['prefixes']:
        print(prefix['ip_prefix'], prefix['region'])
        print("{0}\t{1}".format(prefix['ip_prefix'], prefix['region'])) # with tab
        print("{0},{1}".format(prefix['ip_prefix'], prefix['region'])) # with tab

# print(parcing_url('https://randomuser.me/api/'))
# print(parcing_url_aws('https://ip-ranges.amazonaws.com/ip-ranges.json'))