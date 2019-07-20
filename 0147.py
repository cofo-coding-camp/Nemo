# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        foo = ListNode(0)
        foo.next = head
        pre = head
        cur = head.next

        while cur:
            tail = cur.next
            pre.next = tail
            search = foo
            while search.next and search.next.val < cur.val:
                search = search.next
            
            cur.next = search.next
            search.next = cur
            cur = tail

            if search == pre:
                pre = pre.next
        return foo.next
