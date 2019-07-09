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


# Solution - 2 Binary Insert


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.vec = []

    def binary_insert(self, s, e, tgt):
        while s <= e:
            if s == e:
                if self.vec[s] >= tgt:
                    self.vec.insert(s, tgt)
                else:
                    self.vec.insert(s+1, tgt)
                break
            if e - s == 1 and self.vec[e] > tgt and self.vec[s] < tgt:
                self.vec.insert(s+1, tgt)
                break

            mid = (s + e) // 2

            if self.vec[mid] > tgt:
                e = mid - 1
            elif self.vec[mid] < tgt:
                s = mid + 1
                if self.vec[s] < tgt:
                    pass
                else:
                    self.vec.insert(s, tgt)
                    break
            else:
                self.vec.insert(mid, tgt)

    def addNum(self, num: int) -> None:
        if not self.vec:
            self.vec.append(num)
        elif num >= self.vec[-1]:
            self.vec.append(num)
        elif num <= self.vec[0]:
            self.vec.insert(0, num)
        else:
            self.binary_insert(0, len(self.vec), num)

    def findMedian(self) -> float:
        l = len(self.vec)
        if l % 2:
            return self.vec[l // 2]
        return (self.vec[l // 2 - 1] + self.vec[l // 2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()