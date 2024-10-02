# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        # Create nodes and establish parent-child relationships
        for parentVal, childVal, isLeft in descriptions:
            if parentVal not in nodes:
                nodes[parentVal] = TreeNode(parentVal)
            if childVal not in nodes:
                nodes[childVal] = TreeNode(childVal)

            parentNode = nodes[parentVal]
            childNode = nodes[childVal]

            if isLeft == 1:
                parentNode.left = childNode
            else:
                parentNode.right = childNode

            children.add(childVal)

        # Identify the root node
        root = None
        for parentVal, _, _ in descriptions:
            if parentVal not in children:
                root = nodes[parentVal]
                break

        return root
