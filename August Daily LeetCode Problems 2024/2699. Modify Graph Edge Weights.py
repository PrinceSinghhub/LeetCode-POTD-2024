class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[
        List[int]]:
        adj = [[] for _ in range(n)]

        for idx, (i, j, w) in enumerate(edges):
            if w != -1:
                adj[i].append([j, idx])
                adj[j].append([i, idx])

        def dijkstra(source: int, destination: int) -> int:
            distances = [float('inf') for _ in range(n)]
            distances[source] = 0
            pq = [(0, source)]

            while pq:
                inter_dist, node = heapq.heappop(pq)

                for neighbor, edge_idx in adj[node]:
                    if inter_dist + edges[edge_idx][2] < distances[neighbor]:
                        distances[neighbor] = inter_dist + edges[edge_idx][2]
                        heapq.heappush(pq, (distances[neighbor], neighbor))
            return distances[destination]

        shortest_path_weight_sum = dijkstra(source, destination)

        if shortest_path_weight_sum < target:
            return []

        for idx, (i, j, w) in enumerate(edges):
            if w != -1:
                continue
            if shortest_path_weight_sum == target:
                edges[idx][2] = target + 1
                continue

            w = 1
            edges[idx][2] = w
            adj[i].append([j, idx])
            adj[j].append([i, idx])
            shortest_path_weight_sum = dijkstra(source, destination)

            if shortest_path_weight_sum < target:
                w += target - shortest_path_weight_sum
                edges[idx][2] = w
                shortest_path_weight_sum = target

        if shortest_path_weight_sum == target:
            return edges
        return []