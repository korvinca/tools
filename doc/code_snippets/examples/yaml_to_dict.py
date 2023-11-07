import yaml, json

yaml_text = '''
name: John
age: 30
automobiles:
- brand: Honda
  type: Odyssey
  year: 2018
- brand: Toyota
  type: Sienna
  year: 2015
'''

dict = yaml.safe_load(yaml_text)
# print(str(dict))
# print(len(dict["automobiles"]))
for i in dict["automobiles"]:
    # print(i)
    i["year"] = 2023
    # print(i["brand"])
    # print(i["type"])
    # print(i["year"])
print(str(dict))
print(yaml.dump(dict, default_flow_style=False))

# assert dict['name'] == 'John'
# assert dict['age'] == 30
# assert len(dict["automobiles"]) == 2
# assert dict["automobiles"][0]["brand"] == "Honda"
# assert dict["automobiles"][1]["year"] == 2015
