class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []

        def helper(i, s):
            if i == len(nums):
                res.append(s)
                return
            helper(i + 1, s + [nums[i]])
            helper(i + 1, s)

        helper(0, [])

        return res
