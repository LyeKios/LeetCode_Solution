# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return Solution().isMirror(root, root)

    def isMirror(self, root1, root2):
        if(root1 == None and root2 == None):
            return True
        if(root1 == None or root2 == None):
            return False
        if(root1.val != root2.val):
            return False
        return (Solution().isMirror(root1.left, root2.right) and Solution().isMirror(root2.left, root1.right))