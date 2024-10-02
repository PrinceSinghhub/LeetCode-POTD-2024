class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        output = ""
        for char in order:
            if char in freq:
                output += char * freq[char]
                freq.pop(char)

        for char in freq:
            output += char * freq[char]

        return output