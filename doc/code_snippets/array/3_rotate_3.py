class Solution(object):
    def rotate(self, nums, k): 
        p = len(nums) - 1
        for i in range(len(nums) - k + 1,len(nums) + 1):
            v = nums.pop(p)
            nums.insert(0, v)
        return nums
ob1 = Solution()
print(ob1.rotate([1,2,3,4,5,6,7],3))
print(ob1.rotate([1,2],3))
print(ob1.rotate([1,2,3],8))