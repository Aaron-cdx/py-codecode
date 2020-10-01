# -*- coding:utf-8 -*-
"""
@author caoduanxi
@date   2020/9/29 19:16
Keep thinking, keep coding!
"""
from collections import deque
from typing import List

from Leetcode235_LowestCommonAncestor import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return []
        stack = deque([root])
        while stack:
            # 先放入值
            node = stack.pop()
            res.append(node.val)
            # 然后左右遍历即可
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        # 翻转所有的结果
        return res[::-1]
