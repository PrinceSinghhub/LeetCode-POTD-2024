class Solution:
    def minSwaps(self, s: str) -> int:
        check = []
        for val in s:
            if val == "]" and check and check[-1] == "[":
                check.pop()
            else:
                check.append(val)

        return (len(check) // 2) // 2 + (len(check) // 2 & 1)
