class Solution:
    def isPrefixOfWord(self, s: str, t: str) -> int:
        return next((i for i, w in enumerate(s.split(), 1) if w.startswith(t)), -1)