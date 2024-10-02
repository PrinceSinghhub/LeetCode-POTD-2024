class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        if len(score) > 2:
            arr1 = score.copy()

            arr1.sort()
            arr1 = arr1[::-1]

            f = arr1[0]
            s = arr1[1]
            t = arr1[2]

            ans = [0] * len(score)

            for i in score:
                if i == f:
                    ans[score.index(i)] = "Gold Medal"

                if i == s:
                    ans[score.index(i)] = "Silver Medal"

                if i == t:
                    ans[score.index(i)] = "Bronze Medal"

            print(ans)

            index = 0
            for i in range(len(ans)):
                if ans[i] == 0:
                    ans[i] = score[i]

                index += 1
            print(ans)

            check = ["Gold Medal", "Silver Medal", "Bronze Medal"]
            for i in range(len(ans)):

                if ans[i] not in check:
                    ind = arr1.index(ans[i]) + 1

                    ans[i] = str(ind)

            print(ans)
            return ans

        else:
            if len(score) == 1:
                return ["Gold Medal"]
            else:
                check = ["Gold Medal", "Silver Medal"]
                if score[0] > score[1]:
                    return check
                return check[::-1]
#             check1 = ["Gold Medal","Silver Medal"]

#             for i in range(len(score)):

#                 arr2 = score.copy()

#                 arr2.sort()
#                 arr2 = arr2[::-1]


#                 ans1 = [0] * len(score)

#                 for i in range(len(arr2)):
#                     ind = score.index(arr2[i])
#                     print(ind)
#                     print(check1[ind])
#                     ans1[ind] = check1[ind]

#                 return ans1










