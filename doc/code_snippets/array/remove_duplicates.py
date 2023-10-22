#nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums):
    if len(nums)==0:
        return 0
    if len(nums)==1:
        return nums[0]

print(removeDuplicates([]))
print(removeDuplicates([1]))
print(removeDuplicates([0,0,0,1,1,1,2,2,2]))