class Solution:
    def findJudge(self, n, trust):

        Trust_People = [0] * (n + 1)
        for a, b in trust:
            Trust_People[a] -= 1
            Trust_People[b] += 1

        for i in range(1, n + 1):
            if Trust_People[i] == n - 1:
                return i
        return -1