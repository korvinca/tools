def count_numbers(sorted_list, less_than):
    count = 0
    # for i in sorted_list:
    #     if i < less_than:
    #         count += 1
    #     else:
    #         break
    low = 0
    high = len(sorted_list)
    while low <= high:
        mid = int((low + high) / 2)
        # print(mid)
        if sorted_list[mid] == less_than:
            v = sorted_list[mid]
            count = sorted_list.index(v) - 1
            return count
        elif sorted_list[mid] > less_than:
            v = sorted_list[mid]
            count = sorted_list.index(v)
            # print(count)
            high = mid - 1
        else:
            low = mid + 1
    return count
    

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4)) # should print 2