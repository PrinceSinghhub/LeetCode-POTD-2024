class disjoint_set_union:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0 for i in range(n + 1)]

    def find_parent(self, n):
        if self.parent[n] == n:
            return n
        self.parent[n] = self.find_parent(self.parent[n])
        return self.parent[n]

    def union(self, n1, n2):
        p1 = self.parent[n1]
        p2 = self.parent[n2]
        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            elif self.rank[p2] > self.rank[p1]:
                self.parent[p1] = p2
            else:
                self.parent[p2] = p1
                self.rank[p1] += 1


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings = sorted(meetings, key=lambda x: x[2])

        dsu = disjoint_set_union(n)

        prev = meetings[0][2]
        all = set()
        for i in meetings:
            m1 = i[0]
            m2 = i[1]
            if m1 == 0:
                m1 = firstPerson
            if m2 == 0:
                m2 = firstPerson
            t = i[2]
            if t != prev:
                prev = t
                for j in all:
                    if dsu.find_parent(j) != dsu.find_parent(firstPerson):
                        dsu.parent[j] = j
                        dsu.rank[j] = 0
                all = set()
            all.add(m1)
            all.add(m2)
            # ensuring parent is firstPerson
            if m1 == firstPerson:
                dsu.union(m1, m2)
            else:
                dsu.union(m2, m1)

        ans = [0]
        for i in range(1, n + 1):
            if dsu.find_parent(i) == dsu.find_parent(firstPerson):
                ans.append(i)

        return ans