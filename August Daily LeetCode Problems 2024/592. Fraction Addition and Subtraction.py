import re
from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Find all fractions in the expression
        fractions = re.findall(r'[+-]?\d+/\d+', expression)

        # Initialize the numerator and denominator for the result
        numerator, denominator = 0, 1

        for frac in fractions:
            num, denom = map(int, frac.split('/'))

            # Calculate the new numerator and denominator
            numerator = numerator * denom + num * denominator
            denominator *= denom

            # Simplify the fraction by the greatest common divisor
            common_divisor = gcd(abs(numerator), denominator)
            numerator //= common_divisor
            denominator //= common_divisor

        # Handle the sign of the denominator
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        return f"{numerator}/{denominator}"
