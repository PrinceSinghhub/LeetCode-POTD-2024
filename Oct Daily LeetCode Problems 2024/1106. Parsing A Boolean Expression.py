class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for char in expression:
            if char in ('t', 'f'):
                stack.append(True if char == 't' else False)
            elif char in ('!', '&', '|'):
                stack.append(char)
            elif char == '(':
                stack.append('(')
            elif char == ')':
                sub_expr = []
                while stack[-1] != '(':
                    sub_expr.append(stack.pop())
                stack.pop()
                operator = stack.pop()
                if operator == '!':
                    result = not sub_expr[0]
                elif operator == '&':
                    result = all(sub_expr)
                elif operator == '|':
                    result = any(sub_expr)
                stack.append(result)

        return stack.pop()