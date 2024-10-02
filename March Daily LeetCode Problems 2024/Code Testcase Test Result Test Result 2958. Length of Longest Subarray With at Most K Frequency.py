class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        mpp = {}
        i = 0
        j = 0
        n = len(nums)
        maxx = 0
        while j < n:
            if nums[j] not in mpp:
                mpp[nums[j]] = 0
            mpp[nums[j]] += 1
            while mpp[nums[j]] > k and i < j:
                mpp[nums[i]] -= 1
                i += 1
            maxx = max(maxx, j - i + 1)
            j += 1
        return maxx