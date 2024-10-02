from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum_required = mean * (n + m)
        sum_observed = sum(rolls)
        missing_sum_required = total_sum_required - sum_observed

        # Check if the missing_sum_required is feasible
        if missing_sum_required < n or missing_sum_required > 6 * n:
            return []

        # Initialize the result with 1s
        result = [1] * n
        missing_sum_required -= n

        # Distribute the remaining sum across the result
        for i in range(n):
            add = min(5, missing_sum_required)
            result[i] += add
            missing_sum_required -= add

        return result
