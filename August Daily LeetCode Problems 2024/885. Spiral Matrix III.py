from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = [[rStart, cStart]]
        steps = 1  # Number of steps to take in the current direction
        direction_index = 0  # Start by moving to the right
        r, c = rStart, cStart

        while len(result) < rows * cols:
            for _ in range(2):  # Change direction every two loops
                dr, dc = directions[direction_index]
                for _ in range(steps):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                direction_index = (direction_index + 1) % 4
            steps += 1  # Increase the step count after completing a full cycle

        return result
