class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        store = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def helper(s, i):
            if i == len(digits):
                res.append(s)
                return
            for j in range(len(store[digits[i]])):
                helper(s + store[digits[i]][j], i + 1)

        helper('', 0)

        return res
