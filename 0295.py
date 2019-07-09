# Solution - 1 Priority Queue

import heapq
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_q = []
        self.min_q = []

    def addNum(self, num: int) -> None:
        if not self.max_q:
            heapq.heappush(self.max_q, num)
        elif num >= self.max_q[0]:
            heapq.heappush(self.max_q, num)
        else:
            heapq.heappush(self.min_q, - num)
        while len(self.max_q) - len(self.min_q) >= 2:
            heapq.heappush(self.min_q, - heapq.heappop(self.max_q))
        while len(self.max_q) < len(self.min_q):
            heapq.heappush(self.max_q, - heapq.heappop(self.min_q))

    def findMedian(self) -> float:
        if len(self.max_q) == len(self.min_q):
            return (self.max_q[0] - self.min_q[0]) / 2
        return self.max_q[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
