"""
Given an sorted array of arraies of integers and an integer k, 
return true if k is in array.
"""
# import time

def find_celebrity(nums):
    l = 0
    r = len(nums) - 1
    while l != r:
        if nums[l] not in r:
            l += 1
        else:
            r -= 1
    for i in range(len(nums)):
        if i != l and nums[l] not in nums[l] or nums[l] > nums[i]:
            return "Null"        
    return nums[l]

nums = [1, 5, 9, 13, 15, 18]
print(find_celebrity(nums)) #search
 