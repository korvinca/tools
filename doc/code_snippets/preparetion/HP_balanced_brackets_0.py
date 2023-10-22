'''
balanced string
Given a string A consisting only of '(' and ')'.
You need to find whether parantheses in A is balanced or not,
if it is balanced then return 1 else return 0.
'''

def is_balanced_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return 0  # Unbalanced if closing parenthesis without an opening parenthesis
            stack.pop()
    if not stack:
        return 1
    else:
        return 0   
    #if not stack else 0  # If stack is not empty, then it's unbalanced

# Example usage
# A = "))((()(())"
A = "((()(())))"
result = is_balanced_parentheses(A)
print("Result:", result)

