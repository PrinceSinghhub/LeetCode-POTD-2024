class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj: Dict[int, List[int]] = {}
        rev_adj: Dict[u, Set[int]] = {}
        for i in range(n):
            adj[i] = []
            rev_adj[i] = []

        for u, v in edges:
            adj[u].append(v)

        for i in range(n):
            for child in adj[i]:
                rev_adj[child].append(i)

        mem: Dict[int, List[int]] = {}

        def dfs(node: int) -> List[int]:
            nonlocal mem
            if node in mem:
                return mem[node]
            if not len(rev_adj):
                return []
            result: Set[int] = set()
            for parent in rev_adj[node]:
                result.update(dfs(parent))
                result.add(parent)
            mem[node] = sorted(result)
            return mem[node]

        return [dfs(i) for i in range(n)]

