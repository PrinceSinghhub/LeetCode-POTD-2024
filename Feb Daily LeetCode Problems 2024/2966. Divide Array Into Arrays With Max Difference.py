class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            array = nums[i:i + 3]
            if array[-1] - array[0] > k:
                return None
            res.append(array)
        return res