from collections import defaultdict
class Solution_1:
# Solution 1 - O(n^2)

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        store = defaultdict(int)
        length = 0
        for i in range(len(nums)):
            if store[nums[i]] >= 2:
                for j in range(i + 1, len(nums)):
                    if store[nums[j]] >= 2:
                        continue
                    nums[i], nums[j] = nums[j], nums[i]
                    break
            store[nums[i]] += 1
            if store[nums[i]] <= 2:
                length += 1
        
        return length


class Solution_2:
# Solution 2 - O(n)
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n != nums[i - 2]:
                nums[i] = n
                i += 1
            
        return i
