class Solution(object):
    def postorder(self, root):

        arr = []

        if not root:
            return []

        for node in root.children:
            arr += self.postorder(node)

        arr.append(root.val)

        return arr