class Solution:
    def checkInclusion(self, s1, s2):
        count = {}
        for val in s1:
            count[val] = count.get(val, 0) + 1

        hashet = {}
        sublen = 0

        for i, val in enumerate(s2):
            hashet[val] = hashet.get(val, 0) + 1

            while hashet[val] > count.get(val, 0):
                hashet[s2[i - sublen]] -= 1
                sublen -= 1

            sublen += 1
            if sublen == len(s1):
                return True

        return False