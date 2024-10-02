class Solution:
    def countTriplets(self, arr) -> int:
        count = 0
        len_arr = len(arr)
        for start in range(len_arr - 1):
            res = arr[start]
            for end in range(start + 1, len_arr):
                res ^= arr[end]
                if not res:
                    count += end - start
        return count