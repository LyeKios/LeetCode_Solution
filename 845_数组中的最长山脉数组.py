'''
我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：
B.length >= 3
存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
（注意：B 可以是 A 的任意子数组，包括整个数组 A。）
给出一个整数数组 A，返回最长 “山脉” 的长度。
如果不含有 “山脉” 则返回 0。

示例 1：
输入：[2,1,4,7,3,2,5]
输出：5
解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
示例 2：
输入：[2,2,2]
输出：0
解释：不含 “山脉”。
'''

class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if A == [] or (len(A) <= 2):
            return 0
        ans = 0

        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] and A[i] > A[i + 1]:
                left = i - 1
                right = i + 1
                while (left and A[left - 1] < A[left]): left -= 1
                while (right < len(A)-1 and A[right + 1] < A[right]): right += 1
                ans = max(ans, (right - left +1))
        
        return ans