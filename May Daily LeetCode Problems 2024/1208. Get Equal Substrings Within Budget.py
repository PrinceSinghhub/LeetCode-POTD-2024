class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        left = 0
        currentCost = 0
        maxLength = 0

        for right in range(n):
            # Add the cost of changing s[right] to t[right]
            currentCost += abs(ord(s[right]) - ord(t[right]))

            # If the current cost exceeds maxCost, move the left pointer to the right
            while currentCost > maxCost:
                currentCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            # Update the maximum length of the valid window
            maxLength = max(maxLength, right - left + 1)

        return maxLength