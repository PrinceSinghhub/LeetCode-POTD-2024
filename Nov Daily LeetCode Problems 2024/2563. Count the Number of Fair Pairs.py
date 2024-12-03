from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n):
            low = bisect_left(nums, lower - nums[i], i + 1, n)
            high = bisect_right(nums, upper - nums[i], i + 1, n)
            count += high - low

        return count
