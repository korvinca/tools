"""
Given a sequence of integers as an array, determine whether it is
possible to obtain a strictly 
increasing sequence by removing no more than one element from the array.
"""

def is_increasing(seq):
    for i in range(len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            return False
    return True

def solution(sequence):
    for i in range(len(sequence)):
        modified_seq = sequence[:i] + sequence[i+1:]
        if is_increasing(modified_seq):
            return True
    return False

# Test cases
sequence1 = [1, 3, 2, 1]
print(solution(sequence1))  # Output: False

sequence2 = [1, 3, 2]
print(solution(sequence2))  # Output: True

"""
ou can avoid creating new subarrays for each iteration when checking for strictly increasing sequences. 
Instead, you can maintain a counter to keep track of how many elements you've removed, 
and if you encounter a non-increasing pair, you can make a decision based on the adjacent 
elements without creating new sequences. Here's an optimized version of the code:
"""

def solution_speed(sequence):
    removed_count = 0  # Counter to keep track of removed elements
    
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i - 1]:
            removed_count += 1
            if removed_count > 1:
                return False
            # Check if removing the current element or the previous element
            # would result in a strictly increasing sequence
            if i < 2 or sequence[i] > sequence[i - 2]:
                sequence[i - 1] = sequence[i]
            else:
                sequence[i] = sequence[i - 1]
    return True