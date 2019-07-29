# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h = head
        l = 0
        foo = 1
        while h:
            h = h.next
            l += 1
        res = ListNode(0)
        res.next = head

        while foo < l:
            pre = res
            h = res.next

            while h:
                h1 = h
                i = foo
                while i and h:
                    h = h.next
                    i -= 1
                if i:
                    break
                h2 = h
                i = foo
                while i and h:
                    h = h.next
                    i -= 1

                c1 = foo
                c2 = foo - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next = h1
                        h1 = h1.next
                        c1 -= 1
                    else:
                        pre.next = h2
                        h2 = h2.next
                        c2 -= 1
                    pre = pre.next
                pre.next = h1 if c1 else h2

                while c1 > 0 or c2 > 0:
                    pre = pre.next
                    c1 -= 1
                    c2 -= 1
                pre.next = h
            foo *= 2

        return res.next