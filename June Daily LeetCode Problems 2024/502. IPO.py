class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        capital, profits = zip(*sorted(zip(capital, profits)))
        heap, n, i = [], len(capital), 0

        for _ in range(k):
            while i < n and capital[i] <= w:
                heappush(heap, -profits[i])
                i+=1

            if not heap: break
            w-= heappop(heap)

        return w