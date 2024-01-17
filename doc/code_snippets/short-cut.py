# hashrrank input
if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        print(input())

array=["c","b","a"]
array_d=[3, 2, 1]
array_d.sort()
array.sort()
for i in array:
    print(i)

for i in range(0,len(array)):
    print(array[i])

v = array.pop(len(array) - 1) # delete last
array.insert(0, v) # insert to the first
array.append(v) # append to the end of array
result = ' '.join(v)
# print("Result: ", result, end=" ", "\n")
array=["c","b","a"]
# print(array[0]) #a
# print(array[:1]) #['a']
# print(array[-1]) #c
# print(array[1:]) #['b', 'c']
# print(array[-2:]) #['b', 'c']

# Reverse the list of words
reversed_words = array[::-1]
# Join the reversed words back into a string
reversed_sentence = ' '.join(reversed_words)

for i in array_d:
    pos_inx = array_d.index(i)
    print(pos_inx)
    result = ''.join(i)
print()

hash = set()
for i in array:
    if i in hash:
        continue
    hash.add(i)
print(hash)

#DICTIONARY
d = {}
my_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69}
x=list(my_dict.values())
x.sort(reverse=True)
for j in my_dict.keys():
    print(my_dict[j]) # Print value
# print(d)
for i in my_dict:
	d[i] = None # add key:value - {'A': None, 'B': None}
    my_dict.update({i: 'geeks'}) #{'A': 'geeks', 'B': 'geeks'}
my_dict.pop("A") # Delete key "A"
# print(my_dict)
import json
result = json.dumps(my_dict) # convert to string
# print ("\n", result, "\n") # printing result as string

# STRINGS
# a = "  hello  apple  " # > 'hello  apple'
# b = "  hello  apple  " # > 'helloapple'
# c = "  hello  apple  "
# print(a.strip())
# print(a.replace(" ", ""))
# print(" ".join(a.split()))

def get_content(l):
    line_con = l.split()
    return str(" ".join(line_con[1:]))

lines = logs_txt.splitlines()
data = []
for line in lines:
    if line.startswith("commit"):
        arr_line = line.split()
        comm_id = str(arr_line[1])
        data.append(comm_id)
        if "Author:" in line:
            data.append(get_content(line))

# RE
import re
string = "The quick brown fox jumps over the lazy dog."
# re.sub(pattern, replace, string, count=0, flags=0)
# Replace all occurrences of "the" with "a" using a regular expression
new_string = re.sub("the", "a", string)
new_string = re.sub(r"\b[tT]\w*e\b", "a", string)


#URL FILE OPEN
import urllib.request
import json
with urllib.request.urlopen('https://api.github.com/repos/docker/compose/releases') as response:
    html = response.read()
    data = json.loads(html)
    for i in data :
        print(i['tag_name'])

response = urllib.request.urlopen(url)
body = response.read().decode("utf-8")
data = json.loads(body)
print(data['prefixes'])
for prefix in data['prefixes']:
    print(prefix['ip_prefix'], prefix['region'])
    print("{0}\t{1}".format(prefix['ip_prefix'], prefix['region'])) # with tab
    print("{0}, {1}".format(prefix['ip_prefix'], prefix['region'])) # with tab

with open("data1.json", "r") as mfile:
    content = mfile.read()
    print(type(content))
data = json.loads(content)
# print(type(data))
# print(str(data))

