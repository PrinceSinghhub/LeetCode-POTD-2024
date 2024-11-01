# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q= deque([(root, root.val)])
        while q:
            total = sum([i[0].val for i in q])
            for _ in range(len(q)):
                node, realsum = q.popleft()
                node.val = total - realsum
                realsum= (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                if node.left:   q.append((node.left,realsum))
                if node.right:  q.append((node.right, realsum))
        return root