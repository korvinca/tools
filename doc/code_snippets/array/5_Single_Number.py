class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        j = 0
        for i in range(0, (len(nums)-1)/2):                
            if nums[j] == nums[j+1]:
                j += 2   
                continue
            return nums[j]
        return nums[-1]


ob1 = Solution()
# print(ob1.containsDuplicate([]))
# print(ob1.containsDuplicate([0]))
# print(ob1.containsDuplicate([1,2,3,4,5,6,7]))
print(ob1.containsDuplicate([2,2,1,3]))
print(ob1.containsDuplicate([4,1,2,1,2,4,3]))
print(ob1.containsDuplicate([4,1,2,1,2,3,3]))
