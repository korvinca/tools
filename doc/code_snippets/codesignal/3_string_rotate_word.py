def solution(inputString):
    # result = inputString[::-1] # simple solution
    outputString = []
    for i in inputString:  # iterate to reverse the list
        outputString.insert(0, i) # reversing the list
    result = ''.join(outputString)

    if inputString == result:
        return True
    else:
        return False
    
print(solution("aabaa"))
print(solution("12345"))