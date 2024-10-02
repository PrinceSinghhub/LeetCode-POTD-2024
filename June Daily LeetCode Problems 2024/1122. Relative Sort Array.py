class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        ans = []

        for i in arr2:

            if i in arr1:

                for j in range(arr1.count(i)):
                    ans.append(i)

        remain = []

        for i in arr1:
            if i not in ans:
                remain.append(i)

        remain.sort()

        ans.extend(remain)

        return ans
