class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseMyLinkedList(self, head):
        prevNode = None
        currNode = head

        while currNode is not None:
            nextofNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextofNode
        return prevNode

    def doubleIt(self, head):
        if not head:
            return head

        head = self.reverseMyLinkedList(head)

        currNode = head
        creatNewNode = None
        generateNum = 0

        while currNode is not None:
            doubleNum = currNode.val * 2 + generateNum
            generateNum = doubleNum // 10
            doubleNum %= 10

            if creatNewNode is None:
                creatNewNode = ListNode(doubleNum)
            else:
                generateNode = ListNode(doubleNum)
                generateNode.next = creatNewNode
                creatNewNode = generateNode

            currNode = currNode.next

        if generateNum > 0:
            generateNode = ListNode(generateNum)
            generateNode.next = creatNewNode
            creatNewNode = generateNode

        return creatNewNode
