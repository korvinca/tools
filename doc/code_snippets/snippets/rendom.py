import random

for i in range(10):
    x = random.random()
    print(x)

print (random.randint(5, 10))

t=[1,2,3]
print (random.choice(t))



def generate_random_list(n):
    # Make this function faster.
    # Do not change its output probability distribution.
    result = []
    for i in range(n):
        x = random.randint(1,n)
        if x not in result:
            result.append(x)
    return result

print (generate_random_list(100))
