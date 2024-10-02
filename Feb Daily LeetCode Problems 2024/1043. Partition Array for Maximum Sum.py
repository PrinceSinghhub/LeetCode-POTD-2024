class Solution:
    def maxSumAfterPartitioning(self, A, K):
        dp = [float('-inf') for i in range(len(A) + 1)]
        dp[-1] = 0
        dp[-2] = A[-1]

        for j in reversed(range(len(A) - 1)):
            cur_max = float('-inf')
            for k in range(K):
                if j + k == len(A):
                    break
                cur_max = max(cur_max, A[j + k])
                dp[j] = max(dp[j], (k + 1) * cur_max + dp[j + k + 1])

        return dp[0]
