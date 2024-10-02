class Solution:
    def maxPerimeter(self, nums, dp, n, ans):

        dp[0] = nums[0]
        dirr = [1, 2]

        for i in range(dirr[0], n):
            dp[i] = dp[i - 1] + nums[i]

        for i in range(dirr[1], n):
            if nums[i] < dp[i - 1]:
                ans[0] = max(ans[0], dp[i])

    def largestPerimeter(self, nums):
        nums.sort()
        n = len(nums)
        finalans = [0]
        dp = [0] * n
        self.maxPerimeter(nums, dp, n, finalans)
        if finalans[0] == 0:
            return -1
        return finalans[0]