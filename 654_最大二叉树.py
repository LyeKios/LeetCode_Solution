# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def constructMaxTree(List):
            if List == []:
                return None
            maxNum = max(List)
            maxIndex = List.index(maxNum)

            root = TreeNode(maxNum)
            root.left = constructMaxTree(List[:maxIndex])
            root.right = constructMaxTree(List[maxIndex + 1:])
            return root

        return constructMaxTree(nums)
            