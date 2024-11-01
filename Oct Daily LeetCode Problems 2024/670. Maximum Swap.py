class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))

        last = {int(d): i for i, d in enumerate(digits)}
        for i, d in enumerate(digits):

            for digit in range(9, int(d), -1):
                if last.get(digit, -1) > i:
                    digits[i], digits[last[digit]] = digits[last[digit]], digits[i]
                    return int(''.join(digits))

        return num
