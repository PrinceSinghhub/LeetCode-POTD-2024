class Solution:
    def sortJumbled(self, mapping, nums):

        map_arr = []
        for n in nums:
            n_str = ""
            for i in str(n):
                n_str += str(mapping[int(i)])
            map_arr.append(int(n_str))
        res = list(zip(nums, map_arr))
        res = sorted(res, key=lambda x: x[1])
        res = [i[0] for i in res]
        return res