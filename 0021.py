# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution - 1 Iterative


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = foo = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                foo.next = l1
                l1 = l1.next
                foo = foo.next
            else:
                foo.next = l2
                l2 = l2.next
                foo = foo.next
        foo.next = l1 if l1 else l2
        return head.next


# Sloution - 2 Recursive


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            if not l1 or not l2:
                return l1 or l2
            
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2
            