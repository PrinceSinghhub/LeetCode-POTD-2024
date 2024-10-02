class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res=0
        count=0
        l=0
        m=max(nums)
        n=len(nums)

        for r in range(0,n):
            if nums[r]==m:
                count=count+1
            while count>=k:
                res=res+(n-r)
                if nums[l]==m:
                    count=count-1
                l=l+1

        return res