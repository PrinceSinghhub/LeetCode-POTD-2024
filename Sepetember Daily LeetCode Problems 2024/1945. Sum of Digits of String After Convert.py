class Solution:
    def getLucky(self, s, k):
        s = int(''.join(str(ord(c) - 96) for c in s))
        for i in range(k):
            s_sum = 0
            while s:
                s_sum += s % 10
                s //= 10
            s = s_sum
        return s