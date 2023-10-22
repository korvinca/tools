N = 3


if N % 2 != 0:
    #odd
    print("Weird")
else:
    #even
    if N in range(2,5) or N > 20:
        print("Not Weird")
    else:
        print("Weird")
