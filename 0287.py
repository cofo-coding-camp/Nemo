class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[0]
        slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        p1 = nums[0]
        p2 = slow
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]

        return p1