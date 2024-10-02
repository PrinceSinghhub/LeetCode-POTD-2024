from typing import List
from collections import Counter


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        def word_score(word):
            return sum(score[ord(char) - ord('a')] for char in word)

        def can_form(word, letters_count):
            word_count = Counter(word)
            for char in word_count:
                if word_count[char] > letters_count[char]:
                    return False
            return True

        def backtrack(index, letters_count, current_score):
            nonlocal max_score
            if index == len(words):
                max_score = max(max_score, current_score)
                return

            # Skip current word
            backtrack(index + 1, letters_count, current_score)

            # Include current word if possible
            word = words[index]
            if can_form(word, letters_count):
                # Deduct the letters used by the current word
                for char in word:
                    letters_count[char] -= 1
                # Add the score of the current word
                new_score = current_score + word_score(word)
                backtrack(index + 1, letters_count, new_score)
                # Backtrack (restore the letters count)
                for char in word:
                    letters_count[char] += 1

        letters_count = Counter(letters)
        max_score = 0
        backtrack(0, letters_count, 0)
        return max_score
