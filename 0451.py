from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        res = ''
        if not s:
            return s
        c = Counter(s)
        elem = sorted(c, key= lambda x: c[x])
        while elem:
            i = elem.pop()
            res += i * c[i]
        return res