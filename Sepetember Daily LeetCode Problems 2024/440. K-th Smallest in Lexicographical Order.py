class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # Function to count how many numbers are lexicographically between `prefix` and `prefix + 1`
        def count_steps(prefix, n):
            steps = 0
            first = prefix
            next_prefix = prefix + 1
            while first <= n:
                steps += min(n + 1, next_prefix) - first
                first *= 10
                next_prefix *= 10
            return steps

        curr = 1  # Start with the smallest lexicographical number
        k -= 1  # We start at 1, so we need to find the (k-1)-th number

        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                # If the current prefix and its "children" are fewer than k, skip them
                curr += 1
                k -= steps
            else:
                # Otherwise, go deeper into the current prefix
                curr *= 10
                k -= 1

        return curr
