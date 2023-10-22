"""
Context 
Given a 6x6 2D Array, A:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:
a b c
  d
e f g
There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
Task 
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.
"""


def hourglassSum(arr):
    max_sum = float('-inf')  # Initialize max_sum with negative infinity

    for i in range(4):
        for j in range(4):
            # Calculate the sum of the current hourglass
            current_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
                          arr[i+1][j+1] + \
                          arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            
            # Update max_sum if the current_sum is greater
            max_sum = max(max_sum, current_sum)

    return max_sum

# Input 2D array
arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

# Calculate and print the maximum hourglass sum
result = hourglassSum(arr)
print(result)