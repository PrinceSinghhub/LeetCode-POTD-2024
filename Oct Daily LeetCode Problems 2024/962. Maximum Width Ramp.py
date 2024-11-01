from itertools import accumulate
from operator import sub
from typing import List


class Solution:
    def maxWidthRamp(self, a: List[int]) -> int:
        temp = []
        for i in range(len(a)):
            temp.append((a[i], i))

        temp.sort()

        sorted_indices = []
        for v, i in temp:
            sorted_indices.append(i)

        b = []
        current_min = float('inf')
        for idx in sorted_indices:
            current_min = min(current_min, idx)
            b.append(current_min)

        max_diff = 0
        for i in range(len(sorted_indices)):
            max_diff = max(max_diff, sorted_indices[i] - b[i])

        return max_diff
