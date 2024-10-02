import math as m


class Solution:
    def isPowerOfTwo(self, n):

        index = 0
        while True:

            ans = m.pow(2, index)
            if ans == n:
                return True
            if ans > n:
                return False
            index += 1



