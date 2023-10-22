
def get_biger_int(arr):
    for item in range(0,len(arr) - 1):
        if arr[item] < arr[item+1]:
            print(arr[item], item+1, end=" ")
        else:
            continue
        # for i in arr:
        #     if arr[item] < arr[count]:
        #         print(arr[item], j)
        #     else:
        #         count += 1
            
        # for next_item in range(count, len(arr)-1):
        

        # for next_item in range(0,len(arr)-1):
        #     # print(item,"+",arr[next_item+1],"=",item+arr[next_item+1])
        #     if item + arr[next_item+1] == ask_diget:
        #         res = [item, arr[next_item+1]]
        #         return res
        #     next_item += 1
        # # count += 1
    # return



print(get_biger_int([13, 12, 15, 11, 9, 12, 16]))
# print(find_sum_hash_set([-1, 1, 3, 5, 7],10))
# print(find_sum_binary_search([-7, 0, 2, 3, 6, 8, 10, 15, 18, 20],10))
# print(find_sum_two_markers([-9, -5, -2, -1, 1, 4, 9, 11],3))