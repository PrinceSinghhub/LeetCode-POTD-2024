# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def findGCDVal(self, val1, val2):

        while val1 != val2:

            if val1 > val2:
                val1 = (val1 - val2)

            else:
                val2 = (val2 - val1)

        return val1

    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:

        tempNode = head
        pre_preNodevNode = head.val
        pre_preNode = tempNode
        tempNode = tempNode.next

        while tempNode:
            currNode = tempNode.val
            gcdval = self.findGCDVal(currNode, pre_preNodevNode)

            pre_preNode.next = ListNode(gcdval)
            pre_preNode = pre_preNode.next
            pre_preNode.next = tempNode
            pre_preNode = tempNode
            tempNode = tempNode.next
            pre_preNodevNode = currNode

        return head
