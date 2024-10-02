from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix with infinity and 0s on the diagonal
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        # Fill the distance matrix with the given edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Floyd-Warshall algorithm to find shortest paths between all pairs of cities
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Find the city with the smallest number of neighbors within the threshold distance
        min_neighbors = n
        result_city = -1
        for i in range(n):
            count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            if count <= min_neighbors:
                min_neighbors = count
                result_city = i

        return result_city

# Example usage:
# solution = Solution()
# n = 4
# edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
# distanceThreshold = 4
# print(solution.findTheCity(n, edges, distanceThreshold))  # Output: 3

# n = 5
# edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
# distanceThreshold = 2
# print(solution.findTheCity(n, edges, distanceThreshold))  # Output: 0
