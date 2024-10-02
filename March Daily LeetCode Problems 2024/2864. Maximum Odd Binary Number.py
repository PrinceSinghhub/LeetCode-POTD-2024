class Solution:

    def generateOld(self, s, hasmap):
        oldBin = ""
        N = len(s) - 1

        for _ in range(N):
            if hasmap.get('1') > 1:
                oldBin += '1'
                hasmap['1'] -= 1

            elif hasmap.get('0') >= 1:
                oldBin += '0'
                hasmap['0'] -= 1

        oldBin += '1'
        return oldBin

    def maximumOddBinaryNumber(self, s: str) -> str:
        hasmap = {}
        for data in s:
            if data in hasmap:
                hasmap[data] += 1
            else:
                hasmap[data] = 1

        ans = self.generateOld(s, hasmap)
        return ans