# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(nums):
            if not nums:
                return
            N = len(nums)
            mid = N // 2
            val = nums[mid]
            root = TreeNode(val)
            root.left = helper(nums[:mid])
            root.right = helper(nums[mid + 1:])
            return root
        
        return helper(nums)