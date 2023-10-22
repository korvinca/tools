def solution(picture):
    num = len(picture[0])
    res = []
    res.append("*" * (num + 2))
    for i in picture:
        res.append("*" + i + "*")    
    res.append("*" * (num + 2))
    return res

picture = ["asdfg","12345"]
print(solution(picture))