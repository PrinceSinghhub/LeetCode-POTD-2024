# class Solution:
#     def callfun(self,n,nums):

#         ans = 1
#         for i in range(len(nums)):

#             if i == n:
#                 pass
#             else:
#                 ans*=nums[i]
#         return ans

#     def productExceptSelf(self, nums):


#         ans = []
#         for i in range(len(nums)):
#             element = self.callfun(i,nums)
#             ans.append(element)
#         return ans
class Solution:

    def productExceptSelf(self, nums):

        ans = []
        for i in range(len(nums)):
            ans.append(1)
        left = 1
        for i in range(len(nums)):
            ans[i] = ans[i] * left
            left = left * nums[i]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i] * right
            right = right * nums[i]
        return ans

