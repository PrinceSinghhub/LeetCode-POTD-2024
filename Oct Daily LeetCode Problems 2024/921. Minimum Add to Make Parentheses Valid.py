# class Solution:
#     def minAddToMakeValid(self, s: str) -> int:
#         left = 0
#         right = 0

#         for val in s:
#             if val == '(':
#                 left += 1
#             elif val == ')':
#                 if left > 0:
#                     left -= 1
#                 else:
#                     right += 1
#         return left + right



class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for val in s:
            if val == '(':
                stack.append(val)
            elif val == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(val)
        return len(stack)
