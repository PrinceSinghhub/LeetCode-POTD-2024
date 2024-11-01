from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]

        for j in range(m):
            dp[0][j] = matrix[0][j]
        for i in range(n):
            dp[i][0] = matrix[i][0]

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])

        return sum(sum(row) for row in dp)
