class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        score = 0
        tokens.sort()
        i = 0
        j = len(tokens) - 1
        mx = 0
        while i <= j:
            if tokens[i] <= power:
                power -= tokens[i]
                score += 1
                i += 1
                mx = max(mx, score)
            elif score > 0:
                score -= 1
                power += tokens[j]
                j -= 1
            else:
                break
        return mx