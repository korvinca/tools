def solution(inputArray):
    count = 1
    res = []
    for i in inputArray:
        if len(i) > count:
            count = len(i)
    for i in inputArray:
        if len(i) == count:
            res.append(i)
    return res


def solution_dict(inputArray):
    tmp_dict = {}
    count = 1
    for i in inputArray:
        if len(i) in tmp_dict:
            arr = tmp_dict[len(i)]
            arr.append(i)
            tmp_dict[len(i)] = arr
        else:
            tmp_dict[len(i)] = [i]
        if len(i) > count:
            count = len(i)    
    return tmp_dict[count]

def solution_dict_max(inputArray):
    tmp_dict = {}
    count = 1
    for i in inputArray:
        if len(i) >= count:
            count = len(i)
            if count in tmp_dict:
                arr = tmp_dict[len(i)]
                arr.append(i)
                tmp_dict[count] = arr
            else:
                tmp_dict[count] = [i]
    
    return tmp_dict[count]


array = ["aba", "aa", "ad", "vcd", "aba"]
print(solution(array))
print(solution_dict(array))
print(solution_dict_max(array))