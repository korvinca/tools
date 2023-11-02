"""
BFS
DFS
"""

def maxPathSum(root):
    if not root:
        return False
    
    maxLetfPAth = maxPathSum(root.left)
    maxRightPath = maxPathSum(root.right)
    return max(maxLetfPAth, maxRightPath) + root()

nums = [1, 5, 9, 13, 15, 18]
print(maxPathSum(nums)) #search
