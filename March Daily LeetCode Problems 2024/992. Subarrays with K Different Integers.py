class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            count = 0
            left = 0
            freq = {}

            for right in range(len(nums)):
                if nums[right] not in freq:
                    freq[nums[right]] = 0
                freq[nums[right]] += 1

                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1

                count += right - left + 1

            return count

        return atMostK(nums, k) - atMostK(nums, k - 1)