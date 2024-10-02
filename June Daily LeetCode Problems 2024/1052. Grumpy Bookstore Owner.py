from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        # Step 1: Calculate the initial satisfied customers (where grumpy is 0)
        always_satisfied = sum(customers[i] for i in range(n) if grumpy[i] == 0)

        # Step 2: Calculate the maximum number of additional customers we can satisfy
        #         by applying the technique for 'minutes' consecutive minutes

        # Calculate the initial extra satisfied customers for the first 'minutes' window
        extra_satisfied = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)

        max_extra_satisfied = extra_satisfied

        # Use sliding window to find the maximum extra satisfied customers
        for i in range(minutes, n):
            if grumpy[i] == 1:
                extra_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                extra_satisfied -= customers[i - minutes]
            max_extra_satisfied = max(max_extra_satisfied, extra_satisfied)

        return always_satisfied + max_extra_satisfied

