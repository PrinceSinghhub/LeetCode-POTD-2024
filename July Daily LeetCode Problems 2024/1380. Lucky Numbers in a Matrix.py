# https://leetcode.com/problems/lucky-numbers-in-a-matrix/
class Solution:
    def luckyNumbers(self, matrix):

        l = len(matrix)
        for i in matrix:
            Min = min(i)
            index = i.index(Min)
            temp_arr =[]
            for i in range(l):
                temp_arr.append(matrix[i][index])
            if max(temp_arr)==Min:
                return [Min]
            else:
                temp_arr.clear()


