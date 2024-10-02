class Solution:
    def intersection(self, nums1, nums2):

        A = list(set(nums1))
        B = list(set(nums2))

        ans = []
        for i in A:
            if i in B:
                ans.append(i)
        return ans