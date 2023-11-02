def solution(a):
    res = []
    tree_hash = set()
    for i in range(0,len(a)):
        if a[i] == -1:
            tree_hash.add(i)
        elif a[i] > 0:
            res.append(a[i])
    res.sort()
    if tree_hash:
        for x in tree_hash:
            res.insert(x, -1)
    return res
a = [-1, 150, 180, 170, -1, -1, 200, 190, -1]


"""
To solve this problem, you can follow these steps:

Extract the heights of people from the given list a and store them in a separate list.
Sort the list of people's heights in non-decreasing order.
Iterate through the original list a, and whenever you encounter a -1, pop the smallest height from the sorted list of people's heights and insert it in place of the -1.

"""
def solution_gpt(a):
    # Extract and sort the heights of people (excluding -1)
    # heights = sorted([x for x in a if x != -1])
    heights = []
    for x in a:
        if x != -1:
            heights.append(x)
    heights.sort()
    
    # Initialize an index for the sorted heights list
    height_index = 0
    
    # Iterate through the original list 'a'
    for i in range(len(a)):
        # If the current element is a tree (-1), skip it
        if a[i] == -1:
            continue
        
        # Replace the current element with the next smallest height
        a[i] = heights[height_index]
        height_index += 1
    
    return a

print(solution(a))
print(solution_gpt(a))