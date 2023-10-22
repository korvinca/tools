"""
Given an array of integers, 
find the pair of adjacent elements that has the largest product and return that product.
"""

def solution_sorted(inputArray):
    # for sorter array
    inputArray.sort()
    prod = inputArray[-1] * inputArray[-2]
    return prod

arr = [3, 6, -2, -5, 7, 3]
print("In sorted array: ", solution_sorted(arr), end=" ")
print()

def solution_no_sorted(inputArray):
    prod = inputArray[0] * inputArray[1]
    for i in range(1,len(inputArray)-1):
        in_prod = inputArray[i] * inputArray[i + 1]
        if in_prod > prod:
            prod = in_prod
    return prod

arr = [3, 6, -2, -5, 7, 3]
print("In no sorted array: ", solution_no_sorted(arr), end=" ")