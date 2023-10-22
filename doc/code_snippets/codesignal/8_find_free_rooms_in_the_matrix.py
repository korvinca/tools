
def solution(matrix):
    first_line = 1
    f_cost = 0
    hash = set()
    for sub_array in matrix:
        for i in range(0,len(sub_array)):
            if first_line == 1:
                f_cost += sub_array[i]
                if sub_array[i] == 0 :
                    hash.add(i)
            else:
                if i in hash:
                    continue
                else:
                    f_cost += sub_array[i]
                if sub_array[i] == 0 :
                    hash.add(i)
                
        first_line = 0
    return f_cost


matrix = [[1,1,1], 
          [2,2,2], 
          [3,3,3]]

print(solution(matrix))

