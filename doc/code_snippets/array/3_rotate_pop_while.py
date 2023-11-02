def rotate(nums, k): 
    i = 0
    while i < k:
        v = nums.pop(len(nums) - 1)
        print(v)
        nums.insert(0, v)
        i += 1
    return nums

print(rotate([1,2,3,4,5,6,7],3))
print(rotate([1,2],3))
print(rotate([1,2,3],4))