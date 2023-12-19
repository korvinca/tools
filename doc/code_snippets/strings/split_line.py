# fname = raw_input('Enter the file name: ')

# try:
# 	fhand = open(fname)
# except:
# 	print ('File cannot be opened:'), fname
# 	exit()
# counts = dict()

# for line in fhand:
# 	words = line.split()
# 	for word in words:
# 		if word not in counts:
# 			counts[word] = 1
# 		else:
# 			counts[word] += 1
# print (counts)

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = "smlit me please"
    result = split_and_join(line)
    print(result)