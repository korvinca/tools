class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort() #, reverse=True
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


ob1 = Solution()
print(ob1.containsDuplicate([]))
# print(ob1.containsDuplicate([0]))
# print(ob1.containsDuplicate([1,2,3,4,5,6,7]))
print(ob1.containsDuplicate([4,1,2,3,4,0]))

