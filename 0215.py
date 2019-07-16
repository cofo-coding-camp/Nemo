# Solution Priority Queue


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        q = nums[:k]
        heapq.heapify(q)
        for num in nums[k:]:
            if num > q[0]:
                heapq.heappop(q)
                heapq.heappush(q, num)
        return q[0]
