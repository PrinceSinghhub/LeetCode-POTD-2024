class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_value = (1 << maximumBit) - 1
        cumulative_xor = 0
        for num in nums:
            cumulative_xor ^= num
        result = []
        for num in reversed(nums):
            result.append(cumulative_xor ^ max_value)
            cumulative_xor ^= num

        return result