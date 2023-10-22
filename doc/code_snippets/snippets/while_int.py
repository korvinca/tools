def solution(n):
    res = 10 ** n - 1
    return res

def while_exp(n):
    res = ""
    i = 1
    while i <= n :
        res = res + str(9)
        i += 1
    return int(res)


n = 5
print(solution(n))
print(while_exp(n))