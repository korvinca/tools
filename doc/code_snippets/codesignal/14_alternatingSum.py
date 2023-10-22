def solution(a):
    team_1 = 0
    team_2 = 0
    res = []
    for i in range(0,len(a)):
        if i % 2 == 0:
            team_1 += a[i]
        else:
            team_2 += a[i]
    res.append(team_1)
    res.append(team_2)
    return res
a = [50, 60, 60, 45, 70]
print(solution(a))