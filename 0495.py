class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        if not timeSeries:
            return res
        for i in range(len(timeSeries) - 1):
            if timeSeries[i + 1] - timeSeries[i] >= duration:
                res += duration
            else:
                res += timeSeries[i + 1] - timeSeries[i]
        res += duration
        return res