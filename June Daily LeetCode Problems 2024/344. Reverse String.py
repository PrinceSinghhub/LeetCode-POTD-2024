class Solution:
    def reverseString(self, s):

        # s[:] = s[::-1]
        # return s

        # solve usining swapining
        last = len(s)-1
        start = 0
        while start <= last:
            temp = s[start]
            s[start],s[last] = s[last],temp
            last-=1
            start+=1
        return s