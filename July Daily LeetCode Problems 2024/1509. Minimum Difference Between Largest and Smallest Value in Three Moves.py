class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0

        nums.sort()

        fst = nums[-4] - nums[0]
        scd = nums[-3] - nums[1]
        thrd = nums[-2] - nums[2]
        frth = nums[-1] - nums[3]

        return min(fst, scd, thrd, frth)