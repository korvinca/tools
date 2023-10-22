#Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):        
        if len(nums)==0:
            return 0
        if len(nums)==1:
            nums[0]
            return 1
        prev=nums[0]-1
        count=0
        j=0
        for i,v in enumerate(nums):
            if v!=prev:
                count=count+1
                prev=v
                nums[j]=v
                j=j+1
                # nums = list(dict.fromkeys(nums))
        print(count)
        return count

ob1 = Solution()
ob1.removeDuplicates([1])
ob1.removeDuplicates([1,2,1,5])