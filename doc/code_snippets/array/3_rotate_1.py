class Solution(object):
    def rotate(self, nums, k):
        output_list = [] 

    # Will add values from n to the new list 
        for item in range(len(nums) - k, len(nums)): 
            output_list.append(nums[item]) 

    # Will add the values before 
    # n to the end of new list     
        for item in range(0, len(nums) - k):  
            output_list.append(nums[item]) 
        return output_list


ob1 = Solution()
print(ob1.rotate([1,2,3,4,5,6,7], 3))
print(ob1.rotate([1,2],3))
print(ob1.rotate([1,2,3],8))