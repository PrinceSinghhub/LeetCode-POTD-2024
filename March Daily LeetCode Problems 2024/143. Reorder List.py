# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        q = deque()
        node = head
        while True:
            node = node.next
            if not node:
                break
            q.append(node)

        while q:
            if head:
                temp = q.pop()
                head.next = temp
                head = head.next

            if head and q:
                temp = q.popleft()
                head.next = temp
                head = head.next

        head.next = None