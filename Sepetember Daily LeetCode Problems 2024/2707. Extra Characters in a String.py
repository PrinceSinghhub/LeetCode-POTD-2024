class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        unique = set(dictionary)
        print(unique)

        mydata = [0] * (len(s) + 1)

        for i in range(1, len(s) + 1):

            mydata[i] = mydata[i - 1] + 1

            for j in range(i, 0, -1):

                part = s[j - 1:i]
                if part in unique:
                    mydata[i] = min(mydata[i], mydata[j - 1])
        print(mydata)
        return mydata[len(s)]
