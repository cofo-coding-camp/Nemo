class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-float('inf')] + nums + [-float('inf')]
        left = 0
        right = len(nums) - 1
        while left + 1 != right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid - 1
            elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
                left = mid
            else:
                right = mid