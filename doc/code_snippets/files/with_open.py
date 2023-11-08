import json
with open("data1.json", "r") as mfile:
    content = mfile.read()
    print(type(content))
data = json.loads(content)
print(type(data))
print(str(data))

# with open("data.json") as my_file:
#     for line in my_file:
#         if line:
#             print(line)

# fname = open('mbox-short.txt', 'r')
# for line in fname:
#     print(line, end='')
# # print("\n")