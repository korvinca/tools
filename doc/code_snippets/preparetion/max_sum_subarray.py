'''
Find the contiguous subarray within an array, A of length N which has the largest sum.
A = [1, 2, 3, 4, -10]
Output
Explanation 1:
The subarray [1, 2, 3, 4] has the maximum possible sum of 10.
'''


def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(arr)
print("Maximum subarray sum:", result)