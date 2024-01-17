if __name__ == '__main__':
    N = int(input())
    list=[]
    for _ in range(N):
        n_list = input().split()
        # print(n_list)
        if "insert" == n_list[0]:
            list.insert(int(n_list[1]), int(n_list[2]))
        elif "remove" == n_list[0]:
            if int(n_list[1]) in list:
                list.remove(int(n_list[1]))
        elif "append" == n_list[0]:
            list.append(int(n_list[1]))
        elif "sort" == n_list[0]:
            list.sort()
        elif "pop" == n_list[0]:
            list.pop()
        elif "reverse" == n_list[0]:
            list.reverse()
        elif "print" == n_list[0]:
            print(str(list))