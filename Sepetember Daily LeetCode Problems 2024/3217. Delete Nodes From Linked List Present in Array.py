class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums, head):
        nums_set = set(nums)  # Convert nums list to a set for quick lookup
        dummy = ListNode(0)  # Create a dummy node to help with removing nodes
        dummy.next = head
        current = head
        prev = dummy

        while current:
            if current.val in nums_set:
                prev.next = current.next  # Skip the current node
            else:
                prev = current  # Move prev to the current node
            current = current.next  # Move to the next node

        return dummy.next  # Return the new head of the list
