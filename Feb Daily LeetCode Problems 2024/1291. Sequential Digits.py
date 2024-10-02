class Solution:
    def sequentialDigits(self, low,high):
        num = []
        for x in range(1, 9):
            while x <= high:
                r = x % 10

                if r == 0:
                    break

                if x >= low:
                    num.append(x)

                x = (x * 10) + r + 1

        return sorted(num)