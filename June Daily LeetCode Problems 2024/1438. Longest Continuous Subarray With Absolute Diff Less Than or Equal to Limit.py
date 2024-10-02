from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque = deque()  # to store the minimum values
        max_deque = deque()  # to store the maximum values
        left = 0
        max_length = 0

        for right in range(len(nums)):
            # Maintain the deques
            while min_deque and nums[right] < nums[min_deque[-1]]:
                min_deque.pop()
            while max_deque and nums[right] > nums[max_deque[-1]]:
                max_deque.pop()

            min_deque.append(right)
            max_deque.append(right)

            # If the condition is violated, move the left pointer to shrink the window
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                # Remove elements from deques if they are out of the window
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()

            # Calculate the max length of the subarray
            max_length = max(max_length, right - left + 1)

        return max_length
