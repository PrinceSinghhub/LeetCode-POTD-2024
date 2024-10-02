class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        res = []
        n = len(rowSum)
        m = len(colSum)
        for i in range(n):
            res.append([])
            for j in range(m):
                if rowSum[i] == 0 or colSum[j] == 0:
                    res[-1].append(0)

                else:
                    temp = min(rowSum[i], colSum[j])
                    res[-1].append(temp)
                    rowSum[i] -= temp
                    colSum[j] -= temp
        return res

