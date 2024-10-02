# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sum_map = {0: dummy}

        while head:
            prefix_sum += head.val
            prefix_sum_map[prefix_sum] = head
            head = head.next

        head = dummy
        prefix_sum = 0
        while head:
            prefix_sum += head.val
            if prefix_sum in prefix_sum_map:
                head.next = prefix_sum_map[prefix_sum].next
            head = head.next

        return dummy.next