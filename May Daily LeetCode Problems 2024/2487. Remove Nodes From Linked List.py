# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev, curr = None, node
            while curr:
                nxt = curr.next
                curr.next, prev, curr = prev, curr, nxt
            return prev

        dummy = ListNode()
        dummy.next = reverse(head)
        maxSeen = 0
        prev, curr = dummy, dummy.next

        while curr:
            maxSeen = max(maxSeen, curr.val)
            if curr.val < maxSeen:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return reverse(dummy.next)




