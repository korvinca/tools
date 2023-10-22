# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time


def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)


def nextSquare():
    i = 1
    # An Infinite loop to generate squares
    while True:
        yield i*i
        i += 1  # Next execution resumes
        # from this point

 
# Driver code to test above generator
# function
for num in nextSquare():
    if num > 100:
        break
    print(num)