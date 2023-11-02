with open("data.json") as mfile:
    print(mfile.read())


with open("data.json") as my_file:
    for line in my_file:
        if line:
            print(line)

fname = open('mbox-short.txt', 'r')
for line in fname:
    print(line, end='')
# print("\n")