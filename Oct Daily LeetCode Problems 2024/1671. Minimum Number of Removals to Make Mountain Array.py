from typing import List
from bisect import bisect_left

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        def listRange(nums):
            lis = [1] * n
            temp = []
            for i in range(n):
                pos = bisect_left(temp, nums[i])
                if pos == len(temp):
                    temp.append(nums[i])
                else:
                    temp[pos] = nums[i]
                lis[i] = pos + 1
            return lis

        leftRng = listRange(nums)
        rightRng = listRange(nums[::-1])[::-1]

        ans = float('inf')
        for i in range(1, n - 1):
            if leftRng[i] > 1 and rightRng[i] > 1:
                mountain_len = leftRng[i] + rightRng[i] - 1
                ans = min(ans, n - mountain_len)

        return ans
