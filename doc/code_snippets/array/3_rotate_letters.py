class Solution(object):
    def reverse(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        v = 0
        for i in range(0,len(nums)):
            nums.insert(v,nums.pop(-1))
            v += 1
        # nums.reverse()
        return nums


ob = Solution()
print(ob.reverse([]))
print(ob.reverse(["h"]))
print(ob.reverse(["h","e","l","l","o"]))
print(ob.reverse(["H","a","n","n","a","h"]))