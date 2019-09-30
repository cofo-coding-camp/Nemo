class Solution:
    # Solution 1 - hash table
    def singleNumber(self, nums: List[int]) -> int:
        store = {}
        for i in nums:
            if i in store:
                store.pop(i)
            else:
                store[i] = 1
#            try:
#                store.pop(i)
#            except:
#                store[i] = 1

        return store.popitem()[0]

    
    # Solution 2 - math
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
    
    # Solution 3 - bitwise XOR
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        
        return a
