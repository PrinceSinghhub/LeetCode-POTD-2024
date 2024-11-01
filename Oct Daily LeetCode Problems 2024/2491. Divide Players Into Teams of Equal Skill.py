class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()  # Sort the skill levels to pair smallest with largest
        n = len(skill)
        total_teams = n // 2

        # Calculate the required total skill that every team must have
        total_skill = skill[0] + skill[-1]
        chemistry_sum = 0

        # Iterate over the teams and ensure they all match the total_skill
        for i in range(total_teams):
            # Check if the sum of current pair is equal to the required total_skill
            if skill[i] + skill[n - i - 1] != total_skill:
                return -1  # If any pair doesn't match, return -1

            # Add the chemistry of the current pair (product of their skills)
            chemistry_sum += skill[i] * skill[n - i - 1]

        return chemistry_sum
