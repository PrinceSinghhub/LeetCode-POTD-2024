class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        if ch not in word:
            return word

        ans = ''
        index = -1
        for i in word:
            if i == ch:
                ans += i
                index = word.index(i)
                break
            else:
                ans += i

        ans = ans[::-1] + word[index + 1::]
        return ans

