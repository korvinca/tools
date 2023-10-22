# Python program to show working
# of update() method in Dictionary

# Dictionary with three items
Dictionary1 = {'A': 'Geeks', 'B': 'For', }
Dictionary2 = {'B': 'Geeks'}

# Dictionary before Updation
print("Original Dictionary:")
print(Dictionary1)

# update the value of key 'B'
Dictionary1.update(Dictionary2)
print("Dictionary after updation:")
print(Dictionary1)

## Second
Dictionary1 = {'A': 'Geeks'}
 
# Dictionary before Updation
print("Original Dictionary:")
print(Dictionary1)
 
# update the Dictionary with iterable
Dictionary1.update(B='For', C='Geeks')
print("Dictionary after updation:")
print(Dictionary1)

print("=================================")

def checkKey(dict, key):	
	if key in dict.keys():
		print("Key exist, ", end =" ")
		dict.update({'m':600})
		print("value updated =", 600)
	else:
		print("Not Exist")

dict = {'m': 700, 'n':100, 't':500}
key = 'm'

checkKey(dict, key)
print(dict)