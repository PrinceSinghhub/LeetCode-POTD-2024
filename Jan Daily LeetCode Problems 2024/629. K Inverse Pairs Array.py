class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        m = 10 ** 9 + 7

        dp0 = [0] * (k + 1)
        dp0[0] = 1

        for i in range(n):

            dp1 = []

            s = 0

            for j in range(k + 1):

                s += dp0[j]

                if j >= i + 1:
                    s -= dp0[j - i - 1]

                s %= m

                dp1.append(s)

            dp0 = dp1

        return dp0[-1]