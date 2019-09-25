class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = -1
        n = len(nums)

        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        for i in range(n - 2, -1 , -1):
            if nums[i] < nums[i + 1]:
                first = i
                break
        
        if first == -1:
            reverse(nums, 0, n - 1)
            return

        second = -1
        for i in range(n - 1, first, -1):
            if nums[i] > nums[first]:
                second = i
                break
        nums[first], nums[second] = nums[second], nums[first]

        reverse(nums, first + 1, n - 1)
