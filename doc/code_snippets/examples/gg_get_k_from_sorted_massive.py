"""
Given an sorted array of arraies of integers and an integer k, 
return true if k is in array.
"""
# import time

def find_sum_1(nums,k):
    # st = time.time()
    for i in nums:
        for s_i in i:
            if s_i == k:
                # et = time.time()
                # elapsed_time = et - st
                # print('Execution time:', elapsed_time * 1000, 'milliseconds')
                return "true"
    return "false"

def find_sum_2(nums,k):
    m = len(nums)
    n = len(nums[0])
    for i in range(m):
        l = 0
        r = n - 1
        while l <= r:
            mid = int(l + (r - l) / 2)
            # print(nums[i][mid])
            if nums[i][mid] == k:
                return "true"
            if nums[i][mid] > k:
                r = mid - 1
            else:
                l = mid +1
    return "false"

def find_sum_3(nums,k):
    m = len(nums)
    n = len(nums[0])
    i = 0
    j = n - 1
    while i < m and j >= 0:
        if nums[i][j] == k:
            return "true"
        if nums[i][j] > k:
            j -= 1
        else:
            i += 1
    return "false"

arr = [
    [1, 5, 9, 13],
    [2, 6, 10, 14],
    [3, 7, 11, 15],
    [4, 8, 12, 16]
]

print(find_sum_1(arr,7)) #search
print(find_sum_2(arr,7)) #binary
print(find_sum_3(arr,7)) #diagonal_serch
 