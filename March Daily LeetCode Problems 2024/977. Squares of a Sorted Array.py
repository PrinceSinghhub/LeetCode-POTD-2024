class Solution:
    def sortedSquares(self, nums):
        for key, val in enumerate(nums):
            nums[key] = val * val

        nums.sort()
        return nums
