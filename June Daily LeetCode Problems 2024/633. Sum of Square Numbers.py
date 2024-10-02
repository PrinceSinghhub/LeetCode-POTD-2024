class Solution:
    def judgeSquareSum(self, c):

        ans = set()

        index = 0

        while index * index <= c:
            ans.add(index * index)

            index += 1

        for i in ans:
            if c - i in ans:
                return True

        return False
