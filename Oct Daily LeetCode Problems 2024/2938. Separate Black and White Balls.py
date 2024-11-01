class Solution:
    def minimumSteps(self, s: str) -> int:
        res, swaps = 0, 0
        for ch in s:
            if ch == '1':
                swaps += 1
            else:
                res += swaps
        return res
