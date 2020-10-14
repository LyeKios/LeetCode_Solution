# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return Solution().isBalanceTree(root)[1]
        
    def isBalanceTree(self, root):
        """
        input: [depth, boolean]
        return: [depth, boolean]
        """
        if( root == None):
            return [0, True]
        
        left = Solution().isBalanceTree(root.left)
        right = Solution().isBalanceTree(root.right)
        
        if not (left[1] and right[1]):
            return [0, False]
        if (abs(left[0]-right[0]) > 1):
            return [0, False]
        
        return [max(left[0], right[0]) + 1, True]