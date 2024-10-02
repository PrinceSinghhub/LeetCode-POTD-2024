class UnionFind:

    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = [0] * (n + 1)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])

        return self.parent[u]

    def union(self, u, v):
        parent_u, parent_v = self.find(u), self.find(v)
        if parent_u == parent_v: return False  # cannot union, already unioned!

        if self.rank[u] < self.rank[v]:
            # connect/stick v to u
            self.parent[parent_u] = parent_v
            self.rank[parent_v] += 1

        else:
            # connect u to v
            self.parent[parent_v] = parent_u
            self.rank[parent_u] += 1

        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n + 1)

        b, r, g = 0, 0, 0

        redundant = 0
        # first use the blue ones
        for t, u, v in edges:
            if t == 3:
                if uf.union(u, v):
                    b += 1
                else:
                    redundant += 1
        # make a copy for green ones
        uf2 = copy.deepcopy(uf)

        # now use red ones
        for t, u, v in edges:
            if t == 1:
                if uf.union(u, v):
                    r += 1
                else:
                    redundant += 1

        # now use green ones
        for t, u, v in edges:
            if t == 2:
                if uf2.union(u, v):
                    g += 1
                else:
                    redundant += 1

        if g + b != n - 1 or r + b != n - 1: return -1
        return redundant