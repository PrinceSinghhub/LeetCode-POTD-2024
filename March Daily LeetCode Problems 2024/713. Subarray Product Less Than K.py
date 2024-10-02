class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        first = 0
        second = 0
        product = 1
        combos = 0

        for second in range(len(nums)):

            product *= nums[second]

            while product >= k and first <= second:
                product /= nums[first]
                first += 1

            combos += second - first + 1

        return combos
