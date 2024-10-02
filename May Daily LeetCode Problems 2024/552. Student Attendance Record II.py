class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        if n == 0:
            return 1
        if n == 1:
            return 3  # "P", "L", "A"

        # Initial DP tables
        # dp[i][j][k] - number of sequences of length i with j 'A's and ending with k L's
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]

        # Base case initialization
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for j in range(2):  # number of 'A's
                # Case ending with 'P'
                for k in range(3):
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD

                # Case ending with 'L'
                for k in range(1, 3):
                    dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k - 1]) % MOD

                # Case with one more 'A'
                if j > 0:
                    for k in range(3):
                        dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j - 1][k]) % MOD

        # Sum all valid sequences of length n
        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD

        return result
