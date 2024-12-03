class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1

        min_len = len(nums) + 1
        bit_count = [0] * 32
        left = 0
        n = len(nums)

        for right in range(n):
            or_val = 0
            for i in range(32):
                if nums[right] & (1 << i):
                    bit_count[i] += 1
                if bit_count[i] > 0:
                    or_val |= (1 << i)

            if or_val >= k:
                min_len = min(min_len, right - left + 1)

            while or_val >= k:
                or_val = 0
                for i in range(32):
                    if nums[left] & (1 << i):
                        bit_count[i] -= 1
                    if bit_count[i] > 0:
                        or_val |= (1 << i)

                left += 1
                if or_val >= k:
                    min_len = min(min_len, right - left + 1)

        return -1 if min_len == (len(nums) + 1) else min_len