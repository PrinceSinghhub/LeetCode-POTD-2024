class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        turn, res = 0, 0

        i = 0
        while k > 0:
            val = happiness[i] - turn
            if val >= 0:
                res += val
            turn += 1
            k -= 1
            i += 1

        return res