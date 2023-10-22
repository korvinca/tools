def solution(s1, s2):
    count = 0
    hash = set()
    for i in s1:
        if i in s2:
            if i in hash:
                continue
            hash.add(i)
            count += 1
    return count


s1 = "aabcc"
s2 = "adcaa"
# print(solution(s1, s2))


def solution_gpt(s1, s2):
    char_count_s1 = {}
    char_count_s2 = {}

    # Count character frequencies in s1
    for char in s1:
        char_count_s1[char] = char_count_s1.get(char, 0) + 1
    print(char_count_s1)
    # Count character frequencies in s2
    for char in s2:
        char_count_s2[char] = char_count_s2.get(char, 0) + 1
    print(char_count_s2)
    
    # Initialize a variable to store the count of common characters
    common_count = 0

    # Iterate through characters in s1 and check if they exist in s2
    for char, count in char_count_s1.items():
        if char in char_count_s2:
            common_count += min(count, char_count_s2[char])

    return common_count

result = solution_gpt(s1, s2)
print(result)  # Output: 3