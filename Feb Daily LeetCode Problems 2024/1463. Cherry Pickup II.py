class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memo = {}

        def dp(r, c1, c2):
            if (r, c1, c2) in memo:
                return memo[(r, c1, c2)]


            # Base case: reached the bottom row
            if r == rows:
                return 0

            # Collect cherries from current cells
            cherries = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]

            # Explore all possible movements for both robots
            max_cherries = 0
            for nc1 in [c1 - 1, c1, c1 + 1]:
                for nc2 in [c2 - 1, c2, c2 + 1]:
                    if 0 <= nc1 < cols and 0 <= nc2 < cols:
                        max_cherries = max(max_cherries, dp(r + 1, nc1, nc2))

            # Add collected cherries to the result
            max_cherries += cherries

            # Memoization
            memo[(r, c1, c2)] = max_cherries

            return max_cherries

        return dp(0, 0, cols - 1)

