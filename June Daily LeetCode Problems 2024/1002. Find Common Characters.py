class Solution:
    def commonChars(self, words):

        ans = []

        for i in words[0]:
            flag = True
            for j in range(1, len(words)):
                arr = list(words[j])
                if i in arr:
                    arr.remove(i)
                    temp = "".join(arr)
                    words[j] = temp
                    continue
                else:
                    flag = False
                    break
            if flag == True:
                ans.append(i)
        return ans


