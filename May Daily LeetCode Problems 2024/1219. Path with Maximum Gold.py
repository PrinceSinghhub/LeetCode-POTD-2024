from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def backtrack(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            temp = grid[i][j]
            grid[i][j] = 0
            max_gold = max(backtrack(i+1, j), backtrack(i-1, j), backtrack(i, j+1), backtrack(i, j-1))
            grid[i][j] = temp
            return max_gold + temp

        m, n = len(grid), len(grid[0])
        max_gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, backtrack(i, j))
        return max_gold