class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # think about the example of "12345"
        # case 1: same first half, and palindrome, 123321
        # case 2: first half + 1, and palindrome, 12221
        # case 3: first half - 1, and palindrome, 12421
        # case 4: less digits, and palindrome, 9999
        # case 5: more digits, and palindrome, 100001
        def helper(n, additive):
            l = len(n)
            if l == 0:
                return 0
            first_half = str(int(n[:l // 2 + l % 2]) + additive)
            return int(first_half + first_half[(-1 - l % 2)::-1])

        res = None
        pals = [
            helper(n, 0),
            helper(n, 1),
            helper(n, -1),
            helper("9" * (len(n) - 1), 0),
            helper("1" + "0" * (len(n)), 0)
        ]
        print(pals)
        for i in pals:
            if str(i) == n:
                pass
            else:
                if res is None or abs(res - int(n)) > abs(i - int(n)) or (
                        abs(res - int(n)) == abs(i - int(n)) and i < int(n)):
                    res = i
        return str(res)

