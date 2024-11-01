class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()

        if len(words1) > len(words2):
            words1, words2 = words2, words1

        i = 0

        while i < len(words1) and words1[i] == words2[i]:
            i += 1

        j = len(words1) - 1
        k = len(words2) - 1

        while j >= 0 and words1[j] == words2[k]:
            j -= 1
            k -= 1

        return (i>j)