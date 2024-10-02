class Solution:
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        newls = []
        while head != None:
            newls.append(head.val)
            head = head.next
        newstr = "".join(map(str, newls))
        rootls = [[root, str(root.val)]]
        while len(rootls) != 0:
            root, rootstring = rootls.pop()
            if root != None:
                toadd = rootstring + str(root.val)
                if newstr in toadd:
                    return True
                rootls.append([root.left, toadd])
                rootls.append([root.right, toadd])
        return False
