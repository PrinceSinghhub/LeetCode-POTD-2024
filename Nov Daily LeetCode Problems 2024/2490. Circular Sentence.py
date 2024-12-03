class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        stack = []
        for i, word in enumerate(words):
            if i > 0:
                if stack.pop() != word[0]:
                    return False
            stack.append(word[-1])
        return stack.pop() == words[0][0]
