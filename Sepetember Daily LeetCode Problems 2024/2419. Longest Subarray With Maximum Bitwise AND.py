from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Step 1: Find the maximum value in the array
        max_val = max(nums)

        # Step 2: Traverse the array and find the longest subarray with that max value
        max_len = 0
        current_len = 0

        for num in nums:
            if num == max_val:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 0

        return max_len
