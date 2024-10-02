class Solution:
    def largestLocal(self, grid):
        n = len(grid)
        local_values = []

        for row in range(n - 2):
            local_values.append([])
            for col in range(n - 2):
                row_one = max(grid[row][col : col + 3])
                row_two = max(grid[row + 1][col : col + 3])
                row_three = max(grid[row + 2][col : col + 3])

                max_local = max(row_one, row_two, row_three)
                local_values[row].append(max_local)

        return local_values