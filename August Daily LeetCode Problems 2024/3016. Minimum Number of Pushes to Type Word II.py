class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum([(i // 8 + 1) * val for i, val in enumerate(sorted(list(Counter(word).values()), reverse=True))])