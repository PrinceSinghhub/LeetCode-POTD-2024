import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        ratios = [(w / q, w, q) for w, q in zip(wage, quality)]
        ratios.sort()

        min_wage = float('inf')
        sum_quality = 0
        max_heap = []

        for ratio, w, q in ratios:
            heapq.heappush(max_heap, -q)
            sum_quality += q

            if len(max_heap) > k:
                sum_quality += heapq.heappop(max_heap)

            if len(max_heap) == k:
                min_wage = min(min_wage, sum_quality * ratio)

        return min_wage

