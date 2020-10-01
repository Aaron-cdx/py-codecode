# -*- coding:utf-8 -*-
"""
@author caoduanxi
@date   2020/9/28 10:27
Keep thinking, keep coding!
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """
    python中默认一个变量使用if就代表不为空，如果要对None类型数据进行判断，使用
    if not None => 即可判断是否为None类型类
    """

    def connect(self, root: 'Node') -> 'Node':
        if root is None: return root
        if root.left and root.right:
            root.left.next = root.right
        if root.left and not root.right:
            root.left.next = self.next_node(root.next)
        if root.right:
            root.right.next = self.next_node(root.next)
        self.connect(root.right)
        self.connect(root.left)
        return root

    def next_node(self, node: 'Node') -> 'Node':
        if not node: return node
        if node.left: return node.left
        if node.right: return node.right
        if node.next: return self.next_node(node.next)
        return None
