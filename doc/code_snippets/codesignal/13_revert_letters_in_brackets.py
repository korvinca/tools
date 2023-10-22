def solution(inputString):
    stack = []
    result = ""
    
    for char in inputString:
        if char == '(':
            # Start a new stack for the current open parenthesis
            stack.append(result)
            result = ""
        elif char == ')':
            # Reverse the characters inside the current parenthesis
            result = stack.pop() + result[::-1]
            print(result)
        else:
            # Add characters to the current result
            result += char
    return result
    # res = ""
    # # sub_res[::-1]
    # open_b = []
    # close_b = []
    # for i in inputString:
    #     if i == "(":
    #         open_b.append(i)
    #     elif i == ")":
    #         close_b.append(i)


    # if res == result:
    #     return True
    
inputString = "foo(bar(baz))blim"
result = "foobazrabblim"
print(solution(inputString))