class Solution:
    def frequencySort(self, s):

        # s = "aaahgppppi"
        mydic = Counter(s)

        print(mydic)

        mydic1 = []

        for key, val in mydic.items():
            mydic1.append(val)

        print(mydic1)
        mydic1.sort()

        ans = ""
        for i in mydic1[::-1]:
            for key, val in mydic.items():
                # print(val)
                if i == val:
                    if key in ans:
                        continue
                    else:
                        char = key * i
                        ans += char

        return ans








