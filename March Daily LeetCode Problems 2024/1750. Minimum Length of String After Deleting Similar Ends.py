class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        while len(s) > 1 and s[0] == s[-1]:
            i = 0
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1

            j = len(s) - 1
            while j - 1 > 0 and s[j] == s[j - 1] and j != i:
                j -= 1

            s = s[i + 1:j]

        return len(s)