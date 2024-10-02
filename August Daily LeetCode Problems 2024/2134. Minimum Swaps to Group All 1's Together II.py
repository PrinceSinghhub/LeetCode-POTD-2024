from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        k = sum(nums)  # Total number of 1s in the array

        # If there are no 1s or all are 1s, no swaps are needed
        if k == 0 or k == n:
            return 0

        # Create an extended array to handle the circular nature
        extended_nums = nums + nums[:k-1]

        # Initialize the window
        current_zero_count = sum(1 for i in range(k) if extended_nums[i] == 0)
        min_zero_count = current_zero_count

        # Slide the window over the extended array
        for i in range(1, n):
            # Remove the effect of the element going out of the window
            if extended_nums[i-1] == 0:
                current_zero_count -= 1
            # Add the effect of the new element entering the window
            if extended_nums[i + k - 1] == 0:
                current_zero_count += 1
            # Update the minimum zero count
            min_zero_count = min(min_zero_count, current_zero_count)

        return min_zero_count