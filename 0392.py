class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return False
        i = 0
        j = 0
        while j < len(t):
            if s[i] == t[j]:
                i += 1
                if i == len(s):
                    return True
                j += 1
            else:
                j += 1
        return False