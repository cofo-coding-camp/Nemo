class Solution:
    # Solution 1 - DP
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(n - 1):
            if dp[i]:
                dp[i + 1:i + 1 + nums[i]] = [True] * nums[i]
        
        return dp[-1]

    #Solution 2 - Greedy
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        end = 0
        n = len(nums)

        while start <= end and end <len(nums) - 1:
            end = max(end , nums[start] + start)
            start += 1
        
        return end >= n - 1

    #Solution 3 - Greedy
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        start = n - 2
        end = n - 1
        while start >= 0:
            if start + nums[start] >= end:
                end = start
            start -= 1
        
        return end <= 0