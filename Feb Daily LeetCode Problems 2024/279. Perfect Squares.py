class Solution:
    def numSquares(self, n):

        dp = [float("inf") for i in range(n+1)]
        dp[1] = 1
        perfect = [1]
        for i in range(2,n+1) :
            if not i**0.5 - int(i**0.5):
                dp[i] = 1
                perfect.append(i)
            else:
                for j in perfect:
                    dp[i] = min(dp[i], dp[i-j] + 1)
        return dp[-1]