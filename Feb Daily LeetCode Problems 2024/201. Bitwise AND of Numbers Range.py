class Solution:
    def rangeBitwiseAnd(self, left, right):

        if left == right:
            return right

        while left < right:
            right = right - (right & -right)
        return right