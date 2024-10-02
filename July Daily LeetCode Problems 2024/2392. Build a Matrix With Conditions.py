from collections import defaultdict, deque
from typing import List


class Solution:
    def topological_sort(self, k: int, conditions: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * k

        for u, v in conditions:
            graph[u - 1].append(v - 1)
            indegree[v - 1] += 1

        queue = deque([i for i in range(k) if indegree[i] == 0])
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) == k:
            return topo_order
        else:
            return []

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_order = self.topological_sort(k, rowConditions)
        col_order = self.topological_sort(k, colConditions)

        if not row_order or not col_order:
            return []

        position = {}
        for i, num in enumerate(row_order):
            position[num] = (i, None)
        for i, num in enumerate(col_order):
            if num in position:
                position[num] = (position[num][0], i)
            else:
                position[num] = (None, i)

        matrix = [[0] * k for _ in range(k)]
        for num in range(k):
            if position[num][0] is None or position[num][1] is None:
                return []
            matrix[position[num][0]][position[num][1]] = num + 1

        return matrix
