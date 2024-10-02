class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        # Step 1: Initialize the arrays
        left_b = [0] * (n + 1)  # To handle counts of 'b' to the left of the current position
        right_a = [0] * (n + 1)  # To handle counts of 'a' to the right of the current position

        # Step 2: Populate the left_b array
        for i in range(n):
            left_b[i + 1] = left_b[i] + (1 if s[i] == 'b' else 0)

        # Step 3: Populate the right_a array
        for i in range(n - 1, -1, -1):
            right_a[i] = right_a[i + 1] + (1 if s[i] == 'a' else 0)

        # Step 4: Calculate the minimum deletions required
        min_deletions = float('inf')
        for i in range(n + 1):
            # Deletions to balance up to index i
            deletions = left_b[i] + right_a[i]
            min_deletions = min(min_deletions, deletions)

        return min_deletions

# Example usage
solution = Solution()
s1 = "aababbab"
print(solution.minimumDeletions(s1))  # Output: 2

s2 = "bbaaaaabb"
print(solution.minimumDeletions(s2))  # Output: 2
