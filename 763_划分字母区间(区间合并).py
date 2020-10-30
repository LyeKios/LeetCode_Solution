'''
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。
返回一个表示每个字符串片段的长度的列表。

示例 1：

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
'''

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        h={}#按出现顺序，记录每个字母的最小下标（即第一次出现的下标），与最大下标（即最后一次出现的下标）
        n=len(S)
        for i in range(n):
            if S[i] not in h:
                h[S[i]]=[i,i]#前一个i为最小下标，后一个i为最大下标
            else:
                h[S[i]][1]=i#不断更新最大下标
        # print (h)
        temp1=list(h.values())
        temp = sorted(temp1)
        cur=temp[0]#以第一个元素作为基准
        # print(temp)
        res=[]
        for elem in temp[1:]:
            if elem[0]>cur[1]:#当前元素的初始下标比基准的最大下标，则说明可以分段了
                res.append(cur[1]-cur[0]+1)
                cur = elem#更新基准为当前的元素
            elif elem[1]>cur[1]:#当前元素的初始下标在基准的最小最大之间，但当前元素的最后一次出现下标，
                                #超过当前基准的最大下标，则更新基准的最大下标
                cur[1] = elem[1]
        res.append(cur[1] - cur[0] + 1)#最后一段
        return res