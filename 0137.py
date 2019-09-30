class Solution:
    # Solution 1 - hash table
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}

        for i in nums:
            if i not in hash_table:
                hash_table[i] = 1
            elif hash_table[i] == 1:
                hash_table[i] += 1
            else:
                hash_table.pop(i)
        
        return hash_table.popitem()[0]


    # Solution 2 - bitwise
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0

        for i in nums:
            ones = ones ^ i & ~twos
            twos = twos ^ i & ~ones
        
        return ones