from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Toggle rows to ensure the leftmost digit (column) is 1
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]

        # Toggle columns to maximize the score
        for j in range(1, n):
            count_ones = sum(grid[i][j] for i in range(m))
            if count_ones < m - count_ones:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]

        # Calculate the score
        score = sum(int(''.join(map(str, row)), 2) for row in grid)
        return score