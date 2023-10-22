class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums1.sort()
        nums2.sort()
        p1 = p2 = 0
        result = []

        while p1 < len(nums1) and p2 < len(nums2):
            num1 = nums1[p1]
            num2 = nums2[p2]

            if num1 < num2:
                p1 += 1
            elif num1 > num2:
                p2 += 1
            else:
                result.append(num1)
                p1 += 1
                p2 += 1

        return result

        # # nums1 = list(dict.fromkeys(nums1))
        # for i in range(0,len(nums2)):
        #     t = 0
        #     for n in range(0,len(nums1)):
        #         if t == 1:
        #             continue
        #         if nums1[n] == nums2[i]:
        #             nums_res.append(nums1[n])
        #             t = 1
        # return nums_res

ob1 = Solution()
print(ob1.intersect([1,2,2,1], [3]))
print(ob1.intersect([1,2,2,1], [2]))
print(ob1.intersect([1,2,2,1], [2,2]))
print(ob1.intersect([1,2,2,1], [1,2]))
print(ob1.intersect([4,9,5], [9,4,9,8,4]))
