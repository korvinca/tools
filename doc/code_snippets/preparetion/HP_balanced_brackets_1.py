"""
python3 code for task: given a string with characters '(', ')', '{', '}', '[' and ']'. 
the program must determine whethers the braces are balanced
"""

def is_balanced(expression):
    stack = []
    # Define a mapping of opening to closing braces
    braces_map = {')': '(', '}': '{', ']': '['}
    
    # Iterate through each character in the expression
    for char in expression:
        # If it's an opening brace, push it onto the stack
        if char in '({[':
            stack.append(char)
        # If it's a closing brace
        elif char in ')}]':
            # Check if the stack is empty (unbalanced) or if the top of the stack matches the expected opening brace
            if not stack or stack.pop() != braces_map[char]:
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

