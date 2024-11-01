class Solution:
    def maxMoves(self, grid):
        rows, cols = len(grid), len(grid[0])
        dpTrack = {}
        ans = 0

        def dfs(row, col):
            if (row, col) in dpTrack:
                return dpTrack[(row, col)]

            tempMoves = 0
            for r, c in [(row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]:
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] > grid[row][col]:
                    tempMoves = max(tempMoves, dfs(r, c) + 1)

            dpTrack[(row, col)] = tempMoves
            return tempMoves

        for i in range(rows):
            ans = max(ans, dfs(i, 0))

        return ans
