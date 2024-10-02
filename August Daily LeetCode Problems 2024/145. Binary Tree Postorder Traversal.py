# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):

        # morish Travesrsal  for postOrderTraversal

        postOrder = []

        currNode = root

        while currNode != None:
            if currNode.right == None:
                postOrder.append(currNode.val)
                currNode = currNode.left

            else:
                prevNode = currNode.right
                while prevNode.left != None and prevNode.left != currNode:
                    prevNode = prevNode.left

                # create a thread
                if prevNode.left == None:
                    prevNode.left = currNode
                    postOrder.append(currNode.val)
                    currNode = currNode.right

                else:
                    prevNode.left = None
                    currNode = currNode.left

        return postOrder[::-1]
