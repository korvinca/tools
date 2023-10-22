"""
You can compute the sum of all digits in an integer using Python by converting the integer to a string,
iterating through its characters, and adding their numerical values together. 
Here's a Python code snippet to do that:
"""

# Function to compute the sum of all digits in an integer
def sum_of_digits(n):
    # Convert the integer to a string to iterate through its digits
    n_str = str(n)
    
    # Initialize a variable to store the sum of digits
    digit_sum = 0
    
    # Iterate through each character in the string
    for char in n_str:
        # Check if the character is a digit
        if char.isdigit():
            # Add the numerical value of the digit to the sum
            digit_sum += int(char)
    
    return digit_sum

# Example usage:
integer_value = 12345
result = sum_of_digits(integer_value)
print(f"The sum of digits in {integer_value} is {result}")