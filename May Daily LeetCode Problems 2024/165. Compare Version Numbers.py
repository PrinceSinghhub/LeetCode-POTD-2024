class Solution:
    def compareVersion(self, version1, version2):
        l1 = list(map(int, version1.split('.')))
        l2 = list(map(int, version2.split('.')))
        # print(l1,l2)
        if l1 == l2:
            return (0)

        a = len(l1)
        b = len(l2)

        if a > b:
            for i in range(a - b):
                l2.append("0")

        if b > a:
            for i in range(b - a):
                l1.append("0")

        for i in range(len(l1)):
            if int(l1[i]) > int(l2[i]):
                return (1)

            elif int(l1[i]) < int(l2[i]):
                return (-1)

            else:
                pass

        return (0)