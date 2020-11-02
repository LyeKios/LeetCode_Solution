'''
给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。

 

示例：

输入：[1,2,3,4,5,null,7,8]

        1
       /  \ 
      2    3
     / \    \ 
    4   5    7
   /
  8

输出：[[1],[2,3],[4,5,7],[8]]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        from collections import deque
        if tree is None:
            return []
        res = []  # 结果集
        temp = deque()
        temp.append(tree)
        print (temp)
        while len(temp) > 0:  # BFS模板开始
            tmp_dummy_node = ListNode(None)  # 创建dummynode
            cur = tmp_dummy_node
            next_layer = []  # 存储下一层元素
            while len(temp) != 0:  # 将某一层中的全部取出处理
                node = temp.popleft()
                cur.next = ListNode(node.val)  # 将一层中的组合成链表
                cur = cur.next
                if node.left is not None:
                    next_layer.append(node.left)
                if node.right is not None:
                    next_layer.append(node.right)
            res.append(tmp_dummy_node.next)  # 压入结果集
            temp = deque(next_layer.copy())
        return res
