class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1):
            mod = abs(ord(s[i]) - ord(s[i+1]))
            ans+=mod
        return ans