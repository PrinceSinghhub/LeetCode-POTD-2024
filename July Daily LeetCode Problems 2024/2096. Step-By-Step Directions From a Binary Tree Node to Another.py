# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # Helper function to find the LCA of two nodes
        def findLCA(root, p, q):
            if not root or root.val == p or root.val == q:
                return root
            left = findLCA(root.left, p, q)
            right = findLCA(root.right, p, q)
            if left and right:
                return root
            return left if left else right

        # Helper function to find the path from a node to the target
        def findPath(root, target, path):
            if not root:
                return False
            if root.val == target:
                return True
            path.append('L')
            if findPath(root.left, target, path):
                return True
            path.pop()
            path.append('R')
            if findPath(root.right, target, path):
                return True
            path.pop()
            return False

        # Step 1: Find LCA of startValue and destValue
        lca = findLCA(root, startValue, destValue)

        # Step 2: Find path from LCA to startValue
        path_to_start = []
        findPath(lca, startValue, path_to_start)

        # Step 3: Find path from LCA to destValue
        path_to_dest = []
        findPath(lca, destValue, path_to_dest)

        # Step 4: Convert path_to_start to 'U' and combine with path_to_dest
        path_to_start = ['U'] * len(path_to_start)
        return ''.join(path_to_start + path_to_dest)
