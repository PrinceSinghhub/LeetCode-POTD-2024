from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p

        # If the total sum is already divisible by p, no need to remove any subarray
        if remainder == 0:
            return 0

        # Dictionary to store the most recent index where a particular mod was seen
        prefix_mod = {0: -1}
        current_sum = 0
        min_length = len(nums)  # Start with the maximum possible length

        for i, num in enumerate(nums):
            current_sum += num
            current_mod = current_sum % p

            # We are looking for (current_mod - remainder) % p
            target_mod = (current_mod - remainder) % p

            if target_mod in prefix_mod:
                # Update the minimum length if we found a valid subarray to remove
                min_length = min(min_length, i - prefix_mod[target_mod])

            # Store the current_mod and its index
            prefix_mod[current_mod] = i

        # If min_length is still the maximum length, it means we didn't find any valid subarray
        return min_length if min_length < len(nums) else -1
