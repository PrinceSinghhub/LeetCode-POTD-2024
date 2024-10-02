class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        dp = [1] * len(nums)
        prev_index = [-1] * len(nums)
        max_len = 1
        max_index = 0

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev_index[i] = j
                        if dp[i] > max_len:
                            max_len = dp[i]
                            max_index = i

        subset = []
        while max_index != -1:
            subset.append(nums[max_index])
            max_index = prev_index[max_index]

        return subset[::-1]