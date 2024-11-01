# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heights = {}
        def get_height(node):
            if not node:
                return -1
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            height = 1 + max(left_height, right_height)
            heights[node.val] = height
            return height

        depths = {}
        def dfs(node, depth, max_val):
            if node is None:
                return 

            depths[node.val] = max_val
            dfs(node.left, depth+1, max(max_val, depth+1+(heights[node.right.val] if node.right else -1)))
            dfs(node.right, depth+1, max(max_val, depth+1+(heights[node.left.val] if node.left else -1)))

        get_height(root)
        dfs(root, 0, 0)

        return [depths[q] for q in queries]