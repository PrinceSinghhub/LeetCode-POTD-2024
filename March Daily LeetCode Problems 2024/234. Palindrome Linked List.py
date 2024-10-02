# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        vals = []
        while head:
            vals += head.val,
            head = head.next
        return vals == vals[::-1]
