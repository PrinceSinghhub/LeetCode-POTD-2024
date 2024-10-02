class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Map vowels to bit positions (a=0, e=1, i=2, o=3, u=4)
        vowel_to_bit = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        # Initialize a dictionary to store the first occurrence of each state
        state_to_index = {0: -1}  # Starting state, all vowels have even counts
        current_state = 0  # Starting with no vowels (even counts for all)
        max_len = 0

        # Iterate over the string and update the current state based on vowels
        for i, char in enumerate(s):
            if char in vowel_to_bit:
                # Toggle the corresponding bit in the current state
                current_state ^= vowel_to_bit[char]
            # If the current state has been seen before, calculate the length of the substring
            if current_state in state_to_index:
                max_len = max(max_len, i - state_to_index[current_state])
            else:
                # Store the first occurrence of this state
                state_to_index[current_state] = i

        return max_len
