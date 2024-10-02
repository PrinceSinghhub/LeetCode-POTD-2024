# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node to simplify the result list creation
        current_result = dummy
        current = head.next  # Skip the first zero

        while current:
            sum_val = 0
            # Sum the values until the next zero
            while current and current.val != 0:
                sum_val += current.val
                current = current.next
            # Move to the next node after zero
            current = current.next
            # Create a new node for the sum and attach it to the result list
            new_node = ListNode(sum_val)
            current_result.next = new_node
            current_result = current_result.next

        return dummy.next  # Return the next of dummy node which is the head of the result list

# Helper function to create a linked list from a list of values
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list of values
def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst