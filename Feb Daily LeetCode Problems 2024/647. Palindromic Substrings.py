class Solution:
    def countSubstrings(self, s):
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        count = 0

        for l in range(0, len(s)):  # for different lengths l
            for i in range(len(s) - l):

                j = i + l

                if s[i] == s[j]:
                    if i == j or i == j - 1:  # single and double letters
                        dp[i][j] = True
                    else:  # other cases
                        dp[i][j] = dp[i + 1][j - 1]

                    count += dp[i][j]  # Increasing count if True
        return count
