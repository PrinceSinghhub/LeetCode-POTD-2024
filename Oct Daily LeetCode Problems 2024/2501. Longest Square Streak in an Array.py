class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        square = {}
        nums.sort(reverse=True)
        print(nums)

        res = -1
        for num in nums:
            if num * num in square:
                square[num] = square[num * num] + 1
                res = max(res, square[num])
            else:
                square[num] = 1

        print(square)
        return res