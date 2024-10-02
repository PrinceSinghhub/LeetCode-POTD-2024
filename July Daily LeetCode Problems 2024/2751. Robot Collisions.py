class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # Combine positions, healths, and directions into a single list of tuples
        robots = sorted(zip(positions, healths, directions, range(len(positions))))

        stack = []  # Stack to keep track of robots moving to the right
        survivors = []  # List to keep track of surviving robots

        for pos, health, direction, idx in robots:
            if direction == 'R':
                # If moving to the right, push onto the stack
                stack.append((pos, health, direction, idx))
            else:  # direction == 'L'
                while stack:
                    r_pos, r_health, r_direction, r_idx = stack[-1]
                    if r_direction == 'R':  # Check if top of the stack is moving right
                        if r_health < health:
                            # Remove right moving robot and decrease health of left moving robot
                            stack.pop()
                            health -= 1
                        elif r_health > health:
                            # Decrease health of right moving robot and stop
                            stack[-1] = (r_pos, r_health - 1, r_direction, r_idx)
                            health = 0
                            break
                        else:  # r_health == health
                            # Both robots destroy each other
                            stack.pop()
                            health = 0
                            break
                    else:
                        break
                if health > 0:
                    survivors.append((pos, health, direction, idx))

        # All remaining robots in the stack are survivors moving to the right
        survivors.extend(stack)

        # Sort survivors back to the original input order and extract their healths
        survivors.sort(key=lambda x: x[3])
        return [health for _, health, _, _ in survivors]