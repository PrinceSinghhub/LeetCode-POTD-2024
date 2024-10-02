from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Step 1: Sort dictionary by length of roots for quick lookup
        dictionary = sorted(dictionary, key=len)

        # Step 2: Split the sentence into words
        words = sentence.split()

        # Step 3: Replace words in the sentence
        replaced_sentence = []
        for word in words:
            replaced = word  # Assume no replacement initially
            for root in dictionary:
                if word.startswith(root):
                    replaced = root
                    break
            replaced_sentence.append(replaced)

        # Step 4: Join the words back into a sentence
        return ' '.join(replaced_sentence)
