class Solution:
    # Solution 1 - Binary Search
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        from bisect import bisect_left
        if not nums:
            return 0

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        if nums[-1] < s:
            return 0

        res = float('inf')
        nums = [0] + nums

        for i in range(len(nums)):
            if nums[i] - s >= 0:
                location = bisect_left(nums, nums[i] - s)
                if nums[i] - nums[location] >= s:
                    res = min(res, i - location)
                    continue
                if location > 0:
                    res = min(res, i - location + 1)

        return res if res != float('inf') else 0

    
    # Solution 2 - Sliding Windows
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        left = cur = 0
        res = float('inf')
        for right in range(len(nums)):
            cur += nums[right]
            while cur >= s:
                res = min(res, right - left + 1)
                cur -= nums[left]
                left += 1
        
        return res if res != float('inf') else 0