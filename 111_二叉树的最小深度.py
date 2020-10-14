# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

    def minDepthTree(self, root):
        if (root.right == None or root.left == None):
            return 0
        return min(Solution().minDepthTree(root.left), Solution().minDepthTree(root.right)) + 1