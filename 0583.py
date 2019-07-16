class Solution:
    """
    Transfor into longest common subsequence
    d[i][j] = longest common subsequence of word1[:i] and word2[:j]
    if word1[i-1] == word2[j-1]: d[i][j] = d[i-1][j-1] + 1
    if word1[i-1] != word2[j-1]: max(dp[i-1][j],dp[i][j-1])
    """
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    d[i][j] = d[i - 1][j - 1] + 1
                else:
                    d[i][j] = max(d[i - 1][j], d[i][j - 1])
        
        return n + m - 2 * d[n][m]