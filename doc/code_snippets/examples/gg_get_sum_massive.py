"""
Given an array of integers nums and an integer k, 
return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
"""

def find_sum_1(nums,k):
    answer = 0

    for start in range(len(nums)):
        for end in range(start, len(nums)):
            subarray_sum = 0
            for i in range(start, end + 1):
                subarray_sum += nums[i]
            if subarray_sum == k:
                answer += 1
    return answer

def find_sum_2(nums,k):
    answer = 0

    for start in range(len(nums)):
        subarray_sum = 0
        for i in range(start,len(nums)):
            subarray_sum += nums[i]
            if subarray_sum == k:
                answer += 1
    return answer

def find_sum_3(nums,k):
    answer = 0
    subarray_sum = 0
    prefix_sum_count = {0: 1}

    for i in range(len(nums)):
        subarray_sum += nums[i]
        to_remove = subarray_sum - k
        answer += prefix_sum_count.get(to_remove, 0)
        prev_count = prefix_sum_count.get(subarray_sum, 0)
        prefix_sum_count[subarray_sum] = prev_count + 1

    return answer

print(find_sum_1([7, 2, -5, 1, 1, -1, 5, -5],5))
print(find_sum_2([7, 2, -5, 1, 1, -1, 5, -5],5))
print(find_sum_3([7, 2, -5, 1, 1, -1, 5, -5],5))
 