class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        cur = p1 = 0
        p2 = len(nums) - 1

        while cur <= p2:
            if nums[cur] == 0:
                swap(p1, cur)
                p1 += 1
                cur += 1
            elif nums[cur] == 2:
                swap(cur, p2)
                p2 -= 1
            else:
                cur += 1
            