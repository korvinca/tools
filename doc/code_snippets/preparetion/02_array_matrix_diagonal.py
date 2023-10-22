'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix  is shown below:
1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1+5+9 = 15. The right to left diagonal = 3+5+9 = 17. Their absolute difference is |15 - 17| = 2
'''


def diagonal_difference(matrix):
    n = len(matrix)
    left_to_right_sum = 0
    right_to_left_sum = 0

    for i in range(n):
        left_to_right_sum += matrix[i][i]
        right_to_left_sum += matrix[i][n - 1 - i]

    return abs(left_to_right_sum - right_to_left_sum)

# Example square matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

result = diagonal_difference(matrix)
print(result)