class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        if len(arr) == 3:
            return sum(arr) % 2 != 0

        for i in range(len(arr) - 3):
            if sum(arr[i:i + 3]) % 2 != 0:
                return True

        return False
