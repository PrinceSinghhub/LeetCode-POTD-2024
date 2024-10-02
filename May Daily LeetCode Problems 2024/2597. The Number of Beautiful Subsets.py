class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        @cache
        # ways of choosing from streaks[si][i:]
        def ways(i, si):
            if i >= len(streaks[si]):
                return 1
            # there are 2**rep-1 ways of choosing at least 
            # one of streak[i].
            return ways(i + 1, si) + (2 ** reps[streaks[si][i]] - 1) * ways(i + 2, si)

        reps = defaultdict(int)
        mark = {}  # -1 for start of streak, 1 otherwise

        for num in nums:
            mark[num] = -1

        for num in nums:
            if reps[num]:
                reps[num] += 1
            else:
                if num - k in mark:
                    mark[num] = 1
                reps[num] = 1

        streaks = []
        for num in nums:
            if num not in mark or mark[num] == 1:
                continue
            curr = num
            streaks.append([])
            while curr in mark:
                streaks[-1].append(curr)
                del mark[curr]
                curr = curr + k

        prod = 1
        for i in range(len(streaks)):
            prod *= ways(0, i)
        return prod - 1  # don't consider empty subset