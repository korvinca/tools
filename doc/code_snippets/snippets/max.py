x = max(5, 10)
print(x)

x = max("Mike", "John", "Vicky")
print(x)

a = (1, 5, 3, 9)
x = max(a)
print(x)

def miniMaxSum(arr):
    min_sum = 0
    max_sum = 0
    arr.sort()  # Sort the array in ascending order
    min_sum = sum(arr[:-1])  # Sum of the first four integers (excluding the maximum)
    max_sum = sum(arr[1:])   # Sum of the last four integers (excluding the minimum)
    print(min_sum, max_sum)

arr = [1,2,3,4,5]
miniMaxSum(arr)