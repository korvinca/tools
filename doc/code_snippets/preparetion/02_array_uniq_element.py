# def find_unique_element(arr):
#     unique_element = 0
#     for num in arr:
#         unique_element ^= num  # Using bitwise XOR to cancel out duplicate occurrences
#     return unique_element

# # Example usage
# a = [1, 2, 3, 4, 1, 2, 3]
# result = find_unique_element(a)
# print("The unique element is:", result)

def lonelyinteger(a):
    a.sort()
    for i in a:
        if a.count(i) == 1:
            return i

a = [1, 2, 3, 4, 1, 2, 3, 4, 5]
result = lonelyinteger(a)
print("Uniq:",str(result))