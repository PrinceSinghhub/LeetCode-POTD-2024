from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count_pairs(nums, mid):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count

        nums.sort()
        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            if count_pairs(nums, mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low