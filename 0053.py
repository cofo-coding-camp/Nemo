class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = len(nums) and max(nums)
        pre = 0
        for num in nums:
            pre = max(num, pre + num)
            res = max(res, pre)
        return res