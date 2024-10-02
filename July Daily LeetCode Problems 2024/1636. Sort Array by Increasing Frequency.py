from collections import Counter


class Solution:
    def frequencySort(self, nums):
        d = Counter(nums)

        print(d)

        def check(x):
            return d[x]

        nums.sort(reverse=True)
        nums.sort(key=check)
        return nums

        # brute force approch
        # mydic = {}
        # # key -- count
        # for i in nums:
        #     count = nums.count(i)
        #     mydic[i] = count
        #
        #
        # print(mydic)
        # value = []
        # for key,val in  mydic.items():
        #
        #     value.append(val)
        #
        # value.sort()
        # print(value)
        #
        # finaldic = {}
        # for i in value:
        #     for key, val in mydic.items():
        #         if i == val:
        #             finaldic[key] = val
        # print(finaldic)
        #
        #
        # ans = []
        # for key, value in finaldic.items():
        #     arr = [key, value]
        #     for i in range(value):
        #         ans.append(key)

        # return ans





