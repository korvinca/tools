def find_majority_element_Boyer_Moore(arr):
    count = 0
    candidate = None
    
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1
    
    return candidate

def find_majority_element(arr):
    counts = {}
    n = len(arr)
    
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        if counts[num] > n // 2:
            return num

# Example usage
arr = [2, 2, 3, 3, 2]
majority_element = find_majority_element(arr)
print("Majority element:", majority_element)
