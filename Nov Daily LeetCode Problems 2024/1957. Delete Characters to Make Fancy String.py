class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        count = 1
        stack.append(s[0])
        for i in range(1, len(s)):
            if s[i] == stack[-1]:
                count += 1
            else:
                count = 1

            if count < 3:
                stack.append(s[i])
        return ''.join(stack)