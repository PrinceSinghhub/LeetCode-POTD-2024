# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # for Global Access
    Sum = 0

    def reversePreOrder(self, root):
        if root == None:
            return

        self.reversePreOrder(root.right)
        self.Sum += root.val
        root.val = self.Sum
        self.reversePreOrder(root.left)

        return root

    def bstToGst(self, root: TreeNode) -> TreeNode:
        return self.reversePreOrder(root)


