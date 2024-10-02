from heapq import heappush, heappop
from collections import defaultdict


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Create adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize distances
        dist = [[float('inf')] * 2 for _ in range(n + 1)]
        dist[1][0] = 0

        # Priority queue for Dijkstra's algorithm
        pq = [(0, 1)]  # (time, node)

        while pq:
            t, node = heappop(pq)

            # If we've found the second shortest path to the last node, return
            if node == n and dist[n][1] != float('inf'):
                return dist[n][1]

            # Calculate waiting time due to traffic signal
            if (t // change) % 2 == 1:
                t = (t // change + 1) * change

            # Explore neighbors
            for neighbor in graph[node]:
                new_time = t + time

                if new_time < dist[neighbor][0]:
                    dist[neighbor][1] = dist[neighbor][0]
                    dist[neighbor][0] = new_time
                    heappush(pq, (new_time, neighbor))
                elif dist[neighbor][0] < new_time < dist[neighbor][1]:
                    dist[neighbor][1] = new_time
                    heappush(pq, (new_time, neighbor))

        return -1  # No second shortest path found