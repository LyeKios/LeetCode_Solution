# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 示例 1:
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 示例 2:
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:return
        # 找到中点
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 翻转后半
        pre,cur = None,slow.next
        slow.next = None 
        while cur:
            nxt = cur.next
            cur.next = pre
            pre,cur = cur,nxt
        # 交替合并
        p,q = head,pre
        while q:
            nxt = p.next
            p.next = q
            p,q = q,nxt
        
