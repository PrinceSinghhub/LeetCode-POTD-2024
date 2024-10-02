class Solution:
    def uncommonFromSentences(self, s1, s2):

        ans = []

        lis1 = s1.split(' ')
        lis2 = s2.split(' ')

        for i in lis1:

            if lis1.count(i) == 1 and i not in lis2:
                ans.append(i)

        for i in lis2:

            if lis2.count(i) == 1 and i not in lis1:
                ans.append(i)

        return ans
