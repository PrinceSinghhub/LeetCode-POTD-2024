class Solution:

    def largestNumber(self, nums):


        for i in range(len(nums)):
            for j in range(i+1,len(nums)):

                a,b = str(nums[i]),str(nums[j])
                print(a,b)
                if (int(b+a) > int(a+b)):
                    nums[i],nums[j] = nums[j],nums[i]
        print(nums)


        if nums[0] == 0:
            return '0'

        ans = ""
        for i in nums:
            ans+=str(i)

        return ans