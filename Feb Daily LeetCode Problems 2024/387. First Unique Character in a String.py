from collections import deque


class Solution:
    def firstUniqChar(self, s: str) -> int:

        queue = deque(s)
        print(queue)

        while len(queue) != 0:
            pop = queue.popleft()
            if s.count(pop) == 1:
                return s.index(pop)
        return -1