'''
请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false
示例 2:
输入: 1->2->2->1
输出: true
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        self.list = []
        def createList(node, list):
            if not node : return
            list.append(node.val)
            createList(node.next, list)
            return list

        charList = createList(head, self.list)
        Len = len(charList)

        for i in range(Len/2):
            if not charList[i] == charList[Len - i - 1]:
                return False
        return True