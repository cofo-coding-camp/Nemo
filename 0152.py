class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -float('inf')
        cur_min = 1
        cur_max = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(cur_max * nums[i], nums[i])
            cur_min = min(cur_min * nums[i], nums[i])

            res = max(res, cur_max)

        return res