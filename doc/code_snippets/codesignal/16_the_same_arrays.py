def solution(a, b):
    if len(a) != len(b):
        return False

    diff_count = 0
    diff_indexes = []

    for i in range(len(a)):
        if a[i] != b[i]:
            diff_count += 1
            diff_indexes.append(i)

            if diff_count > 2:
                return False

    if diff_count == 2:
        i, j = diff_indexes
        return a[i] == b[j] and a[j] == b[i]
    elif diff_count == 0:
        # Arrays are identical, no need to swap any elements
        return True
    else:
        return False
    
# Test cases
a1 = [1, 2, 3]
b1 = [1, 2, 3]
print(solution(a1, b1))  # Output should be True

a2 = [1, 2, 3]
b2 = [2, 1, 3]
print(solution(a2, b2))  # Output should be True

a3 = [1, 2, 2]
b3 = [2, 1, 1]
print(solution(a3, b3))  # Output should be False
