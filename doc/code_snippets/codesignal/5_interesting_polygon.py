def solution(n):
    res = n * n + (n - 1) * (n - 1)
    return res

arr = [1,2,3,4,5,6,7,8,9]

for i in arr:
    print(solution(i))