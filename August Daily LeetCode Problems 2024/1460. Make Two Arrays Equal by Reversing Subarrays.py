class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        for i in arr:
            if i in target and arr.count(i) == target.count(i):
                continue
            else:
                return False

        return True

