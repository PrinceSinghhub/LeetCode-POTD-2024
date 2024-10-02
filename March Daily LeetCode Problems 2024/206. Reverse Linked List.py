class Solution:
    def reverseList(self, head):
        node = head
        prev = None
        while node!=None:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev