# import math
# class Solution:
#     def maxKelements(self, nums,k):
#         ans = 0

#         while k != 0:
#             nums.sort()

#             temp = nums.pop()
#             ans += temp

#             temp = math.ceil(temp / 3)

#             nums.append(temp)

#             k-=1

#         return ans

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums.sort()
        score = 0
        while k != 0:
            temp = nums.pop()
            score += temp
            val = math.ceil(temp / 3)
            nums.insert(bisect.bisect(nums, val), val)
            k -= 1
        return score