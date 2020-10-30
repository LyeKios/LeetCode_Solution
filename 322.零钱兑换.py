'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

 

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
示例 4：

输入：coins = [1], amount = 1
输出：1
示例 5：

输入：coins = [1], amount = 2
输出：2
'''

# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         # self.Map = {val:i for i , val in enumerate(coins)}
#         # print self.Map
#         self.Dict = dict()
#         def helper(n):
#             if n in self.Dict: return self.Dict[n]
#             if n == 0: return 0
#             if n < 0: return -1

#             res = float('INF')
#             for coin in coins:
#                 subChange = helper(n - coin)
#                 if subChange == -1: continue
#                 res = min(res, 1+subChange)
#             self.Dict[n] = res if res != float('INF') else -1
#             return self.Dict[n]

#         return helper(amount)

class Solution:
    def coinChange(self, coins, amount):
        # 自底向上
        # dp[i] 表示金额为i需要最少的硬币
        # dp[i] = min(dp[i], dp[i - coins[j]]) j所有硬币
        
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = min(dp[i - c] if i - c >= 0 else float("inf") for c in coins ) + 1
        return dp[-1] if dp[-1] != float("inf") else -1

