class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0

        while s != "1":
            if s[-1] == '0':
                # If the binary number is even, remove the last character (divide by 2)
                s = s[:-1]
            else:
                # If the binary number is odd, we need to add 1
                # This involves a binary addition of 1 to the current binary string
                carry = 1
                s = list(s)
                for i in range(len(s) - 1, -1, -1):
                    if s[i] == '1':
                        s[i] = '0'
                    else:
                        s[i] = '1'
                        carry = 0
                        break
                if carry == 1:
                    s.insert(0, '1')
                s = ''.join(s)
            steps += 1

        return steps