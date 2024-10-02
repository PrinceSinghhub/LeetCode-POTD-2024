from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Initialize the matrix with -1
        matrix = [[-1] * n for _ in range(m)]

        # Define the boundaries
        top, bottom, left, right = 0, m - 1, 0, n - 1

        # Start filling the matrix
        current = head

        while current:
            # Fill top row (left to right)
            for i in range(left, right + 1):
                if current:
                    matrix[top][i] = current.val
                    current = current.next
            top += 1

            # Fill right column (top to bottom)
            for i in range(top, bottom + 1):
                if current:
                    matrix[i][right] = current.val
                    current = current.next
            right -= 1

            # Fill bottom row (right to left)
            for i in range(right, left - 1, -1):
                if current:
                    matrix[bottom][i] = current.val
                    current = current.next
            bottom -= 1

            # Fill left column (bottom to top)
            for i in range(bottom, top - 1, -1):
                if current:
                    matrix[i][left] = current.val
                    current = current.next
            left += 1

        return matrix
