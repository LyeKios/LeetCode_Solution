# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if ((head == None) or (head.next == None)):
            return head
        next = head.next
        head.next = swapPairs(next.next)
        next.next = head 
        return next