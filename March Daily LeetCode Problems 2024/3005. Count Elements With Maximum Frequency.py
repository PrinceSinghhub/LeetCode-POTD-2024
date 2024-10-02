from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        mx = max(count.values())
        return sum(filter(lambda x: x == mx, count.values()))