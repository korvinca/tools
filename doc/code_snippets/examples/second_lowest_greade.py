if __name__ == '__main__':
    # name_dict = {}
    res_list = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     name_dict[name] = score
    name_dict = {'Harry': 37.21, 'Berry': 37.21, 'Tina': 37.2, 'Akriti': 41.0, 'Harsh': 39.0}
    low_n = min(name_dict, key=name_dict.get)
    low_g = name_dict[low_n]

    for n in name_dict.keys():
        name_v = name_dict[n]
        if name_v == low_g:
            res_list.append(n)

    for i in res_list:
        del name_dict[i]

    res_list = []

    low_n = min(name_dict, key=name_dict.get)
    low_g = name_dict[low_n]

    for n in name_dict.keys():
        name_v = name_dict[n]
        if name_v == low_g:
            res_list.append(n)

    res_list.sort()

    for n in res_list:
        print(n)

