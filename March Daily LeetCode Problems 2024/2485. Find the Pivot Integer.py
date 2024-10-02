class Solution:
    def pivotInteger(self, n: int) -> int:

        nums = [i for i in range(1, n + 1)]

        for i in range(n):

            if sum(nums[0:i]) == sum(nums[i + 1::]):
                return nums[i]

        return -1