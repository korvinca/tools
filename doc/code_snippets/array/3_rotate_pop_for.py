
def rotate(nums):
    n = 0
    for i in range(len(nums)):
        v = nums.pop()
        nums.insert(n, v)
        n +=1
    return nums
arr = [1,2,3,4,5,6,7]
print(rotate(arr))
