class Solution(object):
    def minPatches(self, nums, n):
        ans = 0
        sum_val = 1
        m = len(nums)
        i = 0

        while sum_val <= n:
            if i < m and nums[i] <= sum_val:
                sum_val += nums[i]
                i += 1
            else:
                sum_val += sum_val
                ans += 1

        return ans