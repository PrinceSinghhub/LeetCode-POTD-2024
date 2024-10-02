from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def compute(expr: str) -> List[int]:
            # Base case: If the expression is a single number, return it as a list
            if expr.isdigit():
                return [int(expr)]

            # Check if the result is already computed
            if expr in memo:
                return memo[expr]

            results = []
            for i, char in enumerate(expr):
                if char in '+-*':
                    # Split the expression into left and right parts
                    left = expr[:i]
                    right = expr[i + 1:]

                    # Recursively compute results for left and right sub-expressions
                    left_results = compute(left)
                    right_results = compute(right)

                    # Combine results from left and right sub-expressions
                    for l in left_results:
                        for r in right_results:
                            if char == '+':
                                results.append(l + r)
                            elif char == '-':
                                results.append(l - r)
                            elif char == '*':
                                results.append(l * r)

            # Memoize and return results
            memo[expr] = results
            return results

        return compute(expression)
