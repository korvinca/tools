def solution(n):
    n_arr = list(str(n))
    mid = len(n_arr) / 2
    l = 0
    r = 0
    for x in range(0,len(n_arr)):
        if x < mid:
            l += int(n_arr[x])
        else:
            r += int(n_arr[x])
    if l != r:
        return False
    else:
        return True

n = 1234
print(solution(n))
