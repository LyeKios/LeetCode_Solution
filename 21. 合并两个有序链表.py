'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 递归
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def merge(head, l1, l2):
            if l1 != None and l2 != None:
                if l1.val <= l2.val: 
                    head.next = l1
                    merge(head.next, l1.next, l2)
                else: 
                    head.next = l2
                    merge(head.next, l1, l2.next)
            elif l1 == None:
                head.next = l2
            elif l2 == None:
                head.next = l1

        rHead = ListNode(None)
        merge(rHead, l1, l2)
        return rHead.next
    


#迭代
class Solution:
    def mergeTwoLists(self, l1, l2):
        res = ListNode(None)
        node = res
        while l1 and l2:
            if l1.val<l2.val:
                node.next,l1 = l1,l1.next
            else:
                node.next,l2 = l2,l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return res.next