# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 迭代
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead==None or pHead.next==None:
            return pHead
        pre = None
        cur = pHead
        while cur!=None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
    
# 递归
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        pHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return pHead