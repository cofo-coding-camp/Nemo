class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def helper(left):
            i = 0
            j = len(nums)
            while i < j:
                mid = (i + j) // 2
                if nums[mid] == target:
                    if left:
                        j = mid
                    else:
                        i = mid + 1
                elif nums[mid] < target:
                    i = mid + 1
                else:
                    j = mid
            return i
        if not nums:
            return [-1, -1]

        left = helper(True)
        right = helper(False)
        if 0 <= left < len(nums) and nums[left] == target:
            return [left, right - 1]
        else:
            return [-1 , -1]
