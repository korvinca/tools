class Solution:
	# @param A : tuple of integers
	# @return an integer
	def lis(self, A):
		if len(A)==0:
			return 0
		if len(A)==1:
			A[0]
			return 1
		new_array = []
		count = 0
		if type(A)==tuple :
			A = sorted(A)
		else:
			A.sort()

		for i in A:
			if count == 0:
				new_array.append(i)
				count+=1
			if i == new_array[-1]:
				continue
			else:
				if i == new_array[-1] + 1:
					new_array.append(i)
					count+=1
		print(new_array)
		print(count)

ob1 = Solution()
ob1.lis([1,2,1,5])
ob1.lis([ 84, 83, 27 ])
ob1.lis([0, 8, 4, 12, 2, 6, 10, 14, 1, 9, 5, 13, 3, 11, 7, 15, 13, 13])
# print(ob1.lis([1,2,1,5]))
# print(ob1.lis([1,2,1,5]))