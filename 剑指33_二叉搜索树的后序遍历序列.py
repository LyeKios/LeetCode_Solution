'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
参考以下这颗二叉搜索树：
     5
    / \
   2   6
  / \
 1   3
示例 1：
输入: [1,6,3,2,5]
输出: false
示例 2：
输入: [1,3,2,6,5]
输出: true
'''
class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        def isSearch(nums):
            if len(nums) <= 1: return True
            root = nums[-1]
            for i in range(len(nums)):
                if nums[i] > root: break
            for j in range(i, len(nums)-1):
                if nums[j] < root: return False
            return isSearch(nums[:i]) and isSearch(nums[i:-1])
        
        if not postorder: return True
        return isSearch(postorder)