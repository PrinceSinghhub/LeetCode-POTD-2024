class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        x = y = z = 0
        dp = [1] + [0] * (n - 1)
        for i in range(1, n):
            dp[i] = min(dp[x] * 2, dp[y] * 3, dp[z] * 5)
            if dp[i] == dp[x] * 2:
                x += 1
            if dp[i] == dp[y] * 3:
                y += 1
            if dp[i] == dp[z] * 5:
                z += 1
        return dp[-1]
