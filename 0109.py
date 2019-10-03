# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def find_middle(head):
            pre = None
            slow = head
            fast = head

            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            
            if pre:
                pre.next = None
            
            return slow
        
        def helper(head):
            if not head:
                return
            
            mid = find_middle(head)
            root = TreeNode(mid.val)

            if head == mid:
                return root

            root.left = helper(head)
            root.right = helper(mid.next)

            return root
        
        return helper(head)