class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        node1 = edges[0][0]
        node2 = edges[0][1]
        node3 = edges[1][0]
        node4 = edges[1][1]

        # Determine the common node
        if node1 == node3 or node1 == node4:
            return node1
        else:
            return node2