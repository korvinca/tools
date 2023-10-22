# Python code to find key with Maximum value in Dictionary

# Dictionary Initialization
Tv = {'BreakingBad':100, 'GameOfThrones':1292, 'TMKUC' : 88}

Keymax = max(zip(Tv.values(), Tv.keys()))[1]
print(Keymax)


# Python code to find key with Maximum value in Dictionary

# Dictionary Initialization
Company = {'GFG':10000, 'Hashd':2292, 'Infy': 200}

# taking list of car values in v
v = list(Company.values())

# taking list of car keys in v
k = list(Company.keys())

print(k[v.index(max(v))])



# Initialize the dictionary
d = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

# Initialize max_key to the first key in the dictionary
max_key = next(iter(d))

# Iterate over the keys in the dictionary
for key in d:
	# If the value of the current key is greater than the value of max_key, update max_key
	if d[key] > d[max_key]:
		max_key = key

# Print the key with the maximum value
print(max_key)
#This code is contributed by Edula Vinay Kumar Reddy
