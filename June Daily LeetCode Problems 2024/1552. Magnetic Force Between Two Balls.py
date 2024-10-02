from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Sort the positions array
        position.sort()

        # Helper function to check if we can place m balls with at least distance d
        def canPlaceBalls(d):
            count = 1  # Place the first ball in the first basket
            last_position = position[0]

            for i in range(1, len(position)):
                if position[i] - last_position >= d:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True

            return False

        # Binary search for the maximum minimum distance
        left, right = 1, position[-1] - position[0]
        best = 0

        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                best = mid  # Mid is a valid minimum distance, try for a larger one
                left = mid + 1
            else:
                right = mid - 1

        return best
