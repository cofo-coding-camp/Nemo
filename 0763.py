class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        cache = {}
        for i in range(len(S)):
            cache[S[i]] = i

        res = []
        cur = cache[S[0]]

        for i, s in enumerate(S):
            if cache[s] > cur:
                cur = cache[s]
            if i == cur:
                res.append(cur + 1 - sum(res))
        
        return res