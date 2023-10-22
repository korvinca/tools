"""
python3 code for task: given a string with characters '(', ')', '{', '}', '[' and ']'. 
the program must determine whethers the braces are balanced
the same task above but do not use braces_map = {')': '(', '}': '{', ']': '['}
Sure, you can check if the braces in a given string are balanced without using a braces mapping. 
Here's a Python code to do that:
"""



def is_balanced(expression):
    stack = []
    
    # Define the set of opening and closing braces
    opening_braces = '({['
    closing_braces = ')}]'
    
    # Iterate through each character in the expression
    for char in expression:
        # If it's an opening brace, push it onto the stack
        if char in opening_braces:
            stack.append(char)
        # If it's a closing brace
        elif char in closing_braces:
            # Check if the stack is empty (unbalanced)
            if not stack:
                return False
            # Get the corresponding opening brace for the current closing brace
            corresponding_opening_brace = opening_braces[closing_braces.index(char)]
            # Check if the top of the stack matches the expected opening brace
            if stack.pop() != corresponding_opening_brace:
                return False
    
    # After processing all characters, the stack should be empty for a balanced expression
    return len(stack) == 0

# Get the input string from the user
expression = input("Enter a string with braces: ")

result = is_balanced(expression)
if result:
    print(f"The braces in '{expression}' are balanced.")
else:
    print(f"The braces in '{expression}' are not balanced.")

"""
This code checks for balanced braces without using a mapping by using the 
`opening_braces` and `closing_braces` strings to determine 
the correspondence between opening and closing braces.
"""


