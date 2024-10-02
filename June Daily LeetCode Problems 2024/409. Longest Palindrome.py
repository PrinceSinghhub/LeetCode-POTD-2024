class Solution:
    def longestPalindrome(self, s: str) -> int:

        ans = set()

        for i in s:
            if i not in ans:
                ans.add(i)
            else:
                ans.remove(i)

        if len(ans) != 0:
            return len(s) - len(ans) + 1

        return len(s)

