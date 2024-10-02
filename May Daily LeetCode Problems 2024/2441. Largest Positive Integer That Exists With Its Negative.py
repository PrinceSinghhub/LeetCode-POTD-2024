class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        a = []
        c = 0
        for i in nums:
            if i < 0:
                if abs(i) in nums:
                    a.append(abs(i))
                    c += 1
        if c == 0:
            return -1
        else:
            return max(a)
