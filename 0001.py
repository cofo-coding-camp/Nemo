class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, n in enumerate(nums):
            if target - n in store:
                return [store[target - n], i]
            store[n] = i