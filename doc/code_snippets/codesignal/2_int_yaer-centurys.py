def solution(year):
    century = (year - 1) / 100 + 1
    print(century)
    # return int(century)
    century = (year - 1) // 100 + 1
    return century

print(solution(1954))