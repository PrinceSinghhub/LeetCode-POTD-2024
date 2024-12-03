from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def countSetBits(num):
            return bin(num).count('1')

        n = len(nums)
        while True:
            swapped = False
            for i in range(n - 1):
                if countSetBits(nums[i]) == countSetBits(nums[i + 1]) and nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
            if not swapped:
                break

        return nums == sorted(nums)
