# Solution 1 Sliding Window


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        foo = set()
        res = 0
        i = 0
        j = 0

        while i < l and j < l:
            if s[j] not in foo:
                foo.add(s[j])
                j += 1
                res  = max(res, j - i)
            else:
                foo.remove(s[i])
                i += 1
        
        return res

# Solution 2 - Hashtable


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        i = 0
        res = 0
        dic = {}

        for j in range(l):
            if s[j] in dic:
                i = max(i, dic[s[j]])
            res = max(res, j - i + 1)
            dic[s[j]] = j + 1
        
        return res
