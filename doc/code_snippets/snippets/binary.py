"""
Task 
Given a base-10 integer, n, convert it to binary (base-2). 
Then find and print the base-10 integer denoting the maximum number of consecutiv 1's in n's 
binary representation. When working with different bases, 
it is common to show the base as a subscript.
"""


def Binary(n):
    # Initialize variables
    binary_representation = ""
    while n > 0:
        # Build the binary representation in reverse order
        binary_representation = str(n % 2) + binary_representation        
        # Right shift the number
        n //= 2
    return binary_representation

# Metod 1

    # binary_representation = bin(n)[2:]  # Remove the '0b' prefix
    # # Split the binary representation by '0' to get consecutive 1's groups
    # consecutive_ones_groups = binary_representation.split('0')
    # # Find the length of the longest consecutive 1's group
    # # max_consecutive_ones_length = max(len(group) for group in consecutive_ones_groups)
    # arr = []
    # for group in consecutive_ones_groups:
    #     arr.append(len(group))
    # max_consecutive_ones_length = max(arr)
    # return max_consecutive_ones_length

    # arr = []
    # for group in consecutive_ones_groups:
    #     arr.append(len(group))
    # max_consecutive_ones_length = max(arr)
    # return max_consecutive_ones_length

# Metod 2

    # # Initialize variables
    # binary_representation = ""
    # current_consecutive_ones = 0
    # max_consecutive_ones = 0

    # while n > 0:
    #     # Check the least significant bit
    #     if n % 2 == 1:
    #         current_consecutive_ones += 1
    #     else:
    #         current_consecutive_ones = 0
        
    #     # Update the maximum consecutive 1's
    #     max_consecutive_ones = max(max_consecutive_ones, current_consecutive_ones)
        
    #     # Build the binary representation in reverse order
    #     binary_representation = str(n % 2) + binary_representation
        
    #     # Right shift the number
    #     n //= 2
    # return max_consecutive_ones



print(Binary(5))
print(Binary(16))
# print(Binary(14))
