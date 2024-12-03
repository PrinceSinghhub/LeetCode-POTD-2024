class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        n = len(word)

        while i < n:
            char = word[i]
            count = 0
            while i < n and word[i] == char and count < 9:
                count += 1
                i += 1
            comp += str(count) + char

        return comp