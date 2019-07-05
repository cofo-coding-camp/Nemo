# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution - 1 Heapqueue 


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        heap = []
        step = 0
        head = foo = ListNode(0)
        for l in lists:
            while l:
                heapq.heappush(heap, (l.val, step, l))
                l = l.next
                step += 1

        while heap:
            foo.next = heapq.heappop(heap)[-1]
            foo = foo.next

        return head.next


# Solution - 2 Priority Queue


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from queue import PriorityQueue
        pq = PriorityQueue()
        for l in lists:
            if l:
                pq.put((l.val, id(l), l.next))
        head = foo = ListNode(0)
        while not pq.empty():
            val, _, l = pq.get()
            foo.next = ListNode(val)
            foo = foo.next
            if l:
                pq.put((l.val, id(l), l.next))
        return head.next


# Solution - 3 Merge Sort


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
            def merge(list1, list2):
                foo = head = ListNode(0)
                while list1 and list2:
                    if list1.val > list2.val:
                        head.next = list2
                        list2 = list2.next
                    else:
                        head.next = list1
                        list1 = list1.next
                    head = head.next
                head.next = list1 if list1 else list2
                return foo.next
            
            if not lists:
                return None
            if len(lists) == 1:
                return lists[0]
            
            mid = len(lists) // 2
            left = self.mergeKLists(lists[:mid])
            right = self.mergeKLists(lists[mid:])

            return merge(left, right)


# Solution - 4 Brute Force


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        array = []
        for l in lists:
            while l:
                array.append(l.val)
                l = l.next
        array.sort()
        foo = head = ListNode(0)
        for i in array:
            head.next = ListNode(i)
            head = head.next
        return foo.next