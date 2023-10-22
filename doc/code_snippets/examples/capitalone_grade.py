def find_the_best(name_array):
    name_dict = {}
    for i in name_array:
        name = i[:-3]
        grade = int(i[-1])
        if name in name_dict:
            g_arr = name_dict[name]
            g_arr.append(grade)
        else:
            name_dict[name] = [grade]
            
    for i in name_dict:
        name_grade = 0
        res_arr = name_dict[i]
        for x in res_arr:
            name_grade += x
        name_dict[i] = name_grade / len(res_arr)

    # taking list of users values in v
    v = list(name_dict.values())
    print(v)
    print(max(v))

    # taking list of users keys in v
    k = list(name_dict.keys())
    print(k)
    print(v.index(max(v)))

    return k[v.index(max(v))]

example = ["Marry: 3", "Mark: 2", "Bob: 4","John: 5", "John: 4", "John: 5"]
print("Best student:", find_the_best(example))