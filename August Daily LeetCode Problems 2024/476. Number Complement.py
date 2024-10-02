class Solution:
    def findComplement(self, num):

        convert = bin(num)[2::]
        print(convert)

        comp = ""
        for i in convert:
            if i == '0':
                comp += '1'

            elif i == '1':
                comp += '0'

        print(comp)
        ans = int(comp, 2)
        return ans
