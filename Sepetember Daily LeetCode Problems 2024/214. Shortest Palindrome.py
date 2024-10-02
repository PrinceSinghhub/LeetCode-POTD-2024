class Solution:
    def shortestPalindrome(self, s: str) -> str:
        return (r:=s[::-1]) and next(r[:i]+s for i in range(len(s)+1) if s.startswith(r[i:]))