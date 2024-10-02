class Solution:
    def specialArray(self, nums):

        index = 0
        nums.sort()
        nums = nums[::-1]

        while index < len(nums) and nums[index] >= index:
            index += 1

        if nums[index - 1] >= index:
            return index
        return -1

