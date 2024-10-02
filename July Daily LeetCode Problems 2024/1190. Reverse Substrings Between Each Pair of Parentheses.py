class Solution:
    def reverseString(self, s, i, j):
        while i < j:
            if s[i] == '(': i += 1
            if s[j] == ')': j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    def reverseParentheses(self, s):
        st = []
        s = list(s)
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                st.append(i)
            elif s[i] == ')':
                self.reverseString(s, st[-1], i)
                st.pop()

        return ''.join([ch for ch in s if ch.isalpha()])