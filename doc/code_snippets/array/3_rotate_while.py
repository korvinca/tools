def rotate(k): 
    i = len(k)
    res = ""
    arr = []
    while i > 0:
        res = res + str(k[i-1]) + " "
        arr.append(k[i-1])
        i -= 1
    return(arr)

print(rotate([1,2,3,4,5,6,7]))
print(rotate([1,2]))
print(rotate([1,2,3]))
