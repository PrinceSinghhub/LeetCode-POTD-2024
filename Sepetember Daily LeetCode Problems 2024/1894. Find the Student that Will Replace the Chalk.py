from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Step 1: Calculate the total chalk used in one complete round
        total_chalk = sum(chalk)

        # Step 2: Reduce k by the number of complete rounds
        k %= total_chalk

        # Step 3: Find the student who will replace the chalk
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]
