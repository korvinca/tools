
def find_sum_recursive(arr,ask_diget):
    #T O(n2), M O(1)
    # count = 0
    for item in arr:
        # for next_item in range(count, len(arr)-1):
        for next_item in range(0,len(arr)-1):
            # print(item,"+",arr[next_item+1],"=",item+arr[next_item+1])
            if item + arr[next_item+1] == ask_diget:
                res = [item, arr[next_item+1]]
                return res
            next_item += 1
        # count += 1
    return []


def find_sum_hash_set(arr,ask_diget):
    # T O(n), M O(2n)
    # set = [] # create empty hash array
    hash = set() # create empty hash
    for item in arr:
        num_to_find = ask_diget - item 
        # if num_to_find in set:
        if num_to_find in hash:
            return [item,num_to_find]
        else:
            # set.append(item)
            hash.add(item)
            # print(set)
    return []


def find_sum_binary_search(arr,k):
    # T O(n log n), M O(1)
    for item in arr:
        num_to_find = k - item
        l = 1
        r = len(arr) - 1
        while l < r:
            mid = l + (r - l) / 2 # Middle of the search area
            mid_res = arr[int(mid)]
            if mid_res == num_to_find:
                return [item, mid_res]
            if mid_res < num_to_find:
                r = mid - 1
            else:
                l = mid + 1
    return []


def find_sum_two_markers(arr,k):
    # T O(n), M O(1)
    l = 0
    r = len(arr) - 1
    while l < r:
        # print(arr[l])
        # print(arr[r])
        if arr[l] + arr[r] == k:
            return [arr[l], arr[r]]
        elif arr[l] + arr[r] < k:
            l += 1
        else:
            r -= 1
    return []


print(find_sum_recursive([-1, 1, 3, 5, 7],10))
print(find_sum_hash_set([-1, 1, 3, 5, 7],10))
print(find_sum_binary_search([-7, 0, 2, 3, 6, 8, 10, 15, 18, 20],10))
print(find_sum_two_markers([-9, -5, -2, -1, 1, 4, 9, 11],3))