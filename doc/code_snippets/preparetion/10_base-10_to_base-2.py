# # Input a base-10 integer
# n = int(input("Enter a base-10 integer: "))

# # Convert the integer to binary representation
# binary_representation = bin(n)[2:]  # Remove the '0b' prefix

# # Split the binary representation by '0' to get consecutive 1's groups
# consecutive_ones_groups = binary_representation.split('0')

# # Find the length of the longest consecutive 1's group
# max_consecutive_ones_length = max(len(group) for group in consecutive_ones_groups)

# # Print the result
# print("Maximum consecutive 1's in binary representation:", max_consecutive_ones_length)



# Input a base-10 integer
n = int(input("Enter a base-10 integer: "))

# Initialize variables
binary_representation = ""
current_consecutive_ones = 0
max_consecutive_ones = 0

# Calculate the binary representation and find consecutive 1's
while n > 0:
    # Check the least significant bit
    if n % 2 == 1:
        current_consecutive_ones += 1
    else:
        current_consecutive_ones = 0
    
    # Update the maximum consecutive 1's
    max_consecutive_ones = max(max_consecutive_ones, current_consecutive_ones)
    
    # Build the binary representation in reverse order
    binary_representation = str(n % 2) + binary_representation
    
    # Right shift the number
    n //= 2

# Print the binary representation and the maximum consecutive 1's
print("Binary representation:", binary_representation)
print("Maximum consecutive 1's:", max_consecutive_ones)
