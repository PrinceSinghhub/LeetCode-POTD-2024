class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        setsArr = set(spaces)

        for i in range(len(s)):
            if i in setsArr:
                ans.append(' ')
            ans.append(s[i])

        print(ans)
        return ''.join(ans)
