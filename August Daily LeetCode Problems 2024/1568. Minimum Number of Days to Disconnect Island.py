from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def is_connected():
            visited = [[False] * n for _ in range(m)]

            def dfs(x, y):
                if x < 0 or y < 0 or x >= m or y >= n or visited[x][y] or grid[x][y] == 0:
                    return
                visited[x][y] = True
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)

            # Find the first land cell to start DFS
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        dfs(i, j)
                        break
                else:
                    continue
                break

            # Check if there's any land cell that is not visited, meaning it's disconnected
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        return False
            return True

        def count_islands():
            visited = [[False] * n for _ in range(m)]
            islands = 0

            def dfs(x, y):
                if x < 0 or y < 0 or x >= m or y >= n or visited[x][y] or grid[x][y] == 0:
                    return
                visited[x][y] = True
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        islands += 1
                        dfs(i, j)

            return islands

        m, n = len(grid), len(grid[0])

        # If the grid is already disconnected
        if count_islands() != 1:
            return 0

        # Check if we can disconnect the grid by changing one land cell to water
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1

        # If no single change disconnects the grid, it will take at least 2 changes
        return 2
