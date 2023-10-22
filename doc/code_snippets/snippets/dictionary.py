# Python3 code to demonstrate working of
# Perform operation on each key dictionary
# Using loop

# Initialize dictionary
test_dict = {'gfg' : 6, 'is' : 4, 'best' : 7}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Using loop
# Perform operation on each key dictionary
for key in test_dict:	
	test_dict[key] *= 3

# printing result
print("The dictionary after triple each key's value : " + str(test_dict))
