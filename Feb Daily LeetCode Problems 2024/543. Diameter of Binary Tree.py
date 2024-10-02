# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findDiameter(self, root, Max):
        if root == None:
            return 0

        left = self.findDiameter(root.left, Max)
        right = self.findDiameter(root.right, Max)

        Max[0] = max(Max[0], left + right)

        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        Max = [0]

        self.findDiameter(root, Max)
        return Max[0]


