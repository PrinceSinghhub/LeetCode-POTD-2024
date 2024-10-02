class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        mydic = {}
        for val in nums:
            if val in mydic:
                mydic[val] += 1
            else:
                mydic[val] = 1

        ans = [data for data, count in mydic.items() if count > 1]
        return ans
