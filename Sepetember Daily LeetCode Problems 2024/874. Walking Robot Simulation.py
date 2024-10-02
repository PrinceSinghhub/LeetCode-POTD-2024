from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_index = 0  # Start facing North
        x, y = 0, 0  # Start position
        obstacle_set = set(map(tuple, obstacles))  # Convert obstacles to a set of tuples
        max_distance_squared = 0

        for command in commands:
            if command == -2:  # Turn left
                direction_index = (direction_index - 1) % 4
            elif command == -1:  # Turn right
                direction_index = (direction_index + 1) % 4
            else:
                dx, dy = directions[direction_index]
                for _ in range(command):
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        max_distance_squared = max(max_distance_squared, x * x + y * y)
                    else:
                        break

        return max_distance_squared
