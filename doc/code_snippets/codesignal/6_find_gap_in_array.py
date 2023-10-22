"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday,
each statue having an non-negative integer size. 
Since he likes to make things perfect,
he wants to arrange them from smallest to largest so that each 
statue will be bigger than the previous one exactly by 1. 
He may need some additional statues to be able to accomplish that. 
Help him figure out the minimum number of additional statues needed.
"""

def solution(statues):
    statues.sort()
    count = 0
    for i in range(0,len(statues)-1):
        tmp_count = statues[i + 1] - statues[i] - 1
        if tmp_count == 0:
            continue
        else:
            count += tmp_count
    return count

print(solution([6, 2, 3, 8]))
print(solution([0, 3]))
print(solution([5,4,6]))