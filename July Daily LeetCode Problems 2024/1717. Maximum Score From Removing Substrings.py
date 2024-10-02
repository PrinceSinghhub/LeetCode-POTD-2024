class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, sub, points):
            stack = []
            score = 0
            for char in s:
                stack.append(char)
                if len(stack) >= 2 and stack[-2] + stack[-1] == sub:
                    stack.pop()
                    stack.pop()
                    score += points
            return "".join(stack), score

        if x >= y:
            s, score1 = remove_substring(s, "ab", x)
            s, score2 = remove_substring(s, "ba", y)
        else:
            s, score1 = remove_substring(s, "ba", y)
            s, score2 = remove_substring(s, "ab", x)

        return score1 + score2
