class Solution:
    def minSteps(self, n: int) -> int:
        result = 0
        cur_copy = 0
        cur_len = 1
        n -= 1
        while n > 0:
            if n % cur_len == 0:
                cur_copy = cur_len
                result += 2
            else:
                result += 1
            n -= cur_copy
            cur_len += cur_copy
        return result