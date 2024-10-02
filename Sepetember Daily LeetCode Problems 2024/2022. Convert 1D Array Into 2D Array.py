class Solution:
    def construct2DArray(self, original, m, n):
        size = len(original)
        if (m * n != size):
            return []

        if m == 1:
            return [original]

        ans = []
        for row in range(0, size, n):
            print(row)
            temp = original[row: row + n]
            ans.append(temp)
        return ans