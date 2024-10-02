class Solution:

    def findAllcombinationSum(self, index, candidates, target, ans, ds):

        if target == 0:
            ans.append(ds[:])
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > target:
                break

            ds.append(candidates[i])
            self.findAllcombinationSum(i + 1, candidates, target - candidates[i], ans, ds)
            ds.pop()

    def combinationSum2(self, candidates, target):

        ans = []
        candidates.sort()

        self.findAllcombinationSum(0, candidates, target, ans, [])
        return ans