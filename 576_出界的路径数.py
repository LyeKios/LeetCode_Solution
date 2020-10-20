'''
给定一个 m × n 的网格和一个球。球的起始坐标为 (i,j) ，你可以将球移到相邻的单元格内,
或者往上、下、左、右四个方向上移动使球穿过网格边界。但是，你最多可以移动 N 次。
找出可以将球移出边界的路径数量。答案可能非常大，返回 结果 mod 109 + 7 的值。

 

示例 1：

输入: m = 2, n = 2, N = 2, i = 0, j = 0
输出: 6

'''



class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [{} for _ in range(N + 1)]
        dp[0][(i, j)] = 1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0
        for step in range(1, N + 1):
            for r, c in dp[step - 1]:
                count = dp[step - 1][(r, c)]
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if nr >= m or nc >= n or nr < 0 or nc < 0:
                        ans += count
                        ans %= (10 ** 9 + 7)
                    elif (nr, nc) in dp[step]:
                        dp[step][(nr, nc)] += count
                    else:
                        dp[step][(nr, nc)] = count
        return ans % 1000000007