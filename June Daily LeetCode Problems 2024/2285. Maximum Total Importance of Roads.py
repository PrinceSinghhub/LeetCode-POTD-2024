from audioop import mul
from collections import Counter
from itertools import count


class Solution:
    def maximumImportance(self, n, R):
        return -sum(map(mul, count(-n), sorted(Counter(x for r in R for x in r).values(), reverse=1)))
