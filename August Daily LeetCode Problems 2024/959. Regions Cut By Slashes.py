from typing import List


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.count = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1

    def get_count(self):
        return self.count


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UnionFind(n * n * 4)

        for r in range(n):
            for c in range(n):
                root = 4 * (r * n + c)
                val = grid[r][c]

                # Connect the internal edges based on the character
                if val == '/':
                    uf.union(root + 0, root + 3)
                    uf.union(root + 1, root + 2)
                elif val == '\\':
                    uf.union(root + 0, root + 1)
                    uf.union(root + 2, root + 3)
                else:  # ' '
                    uf.union(root + 0, root + 1)
                    uf.union(root + 1, root + 2)
                    uf.union(root + 2, root + 3)

                # Connect edges with the neighboring cells
                if r + 1 < n:
                    uf.union(root + 2, root + 4 * n + 0)
                if c + 1 < n:
                    uf.union(root + 1, root + 4 + 3)

        return uf.get_count()

