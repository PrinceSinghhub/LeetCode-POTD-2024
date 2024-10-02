class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        current = list1
        count = 0

        while count < a - 1:
            current = current.next
            count += 1

        start = current

        while count < b + 1:
            current = current.next
            count += 1

        end = current

        start.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = end

        return list1
