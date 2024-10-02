class Solution:

    def partitionString(self, index, s, path, res):

        if index == len(s):
            res.append(path[:])
            return

        for i in range(index, len(s)):
            if self.isPalindrome(s, index, i):
                path.append(s[index:i + 1])
                self.partitionString(i + 1, s, path, res)
                path.pop()

    def isPalindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:

        res = []
        path = []

        self.partitionString(0, s, path, res)
        return res