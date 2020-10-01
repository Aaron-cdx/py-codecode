# -*- coding:utf-8 -*-
from Leetcode235_LowestCommonAncestor import TreeNode

"""
@author caoduanxi
@date   2020/9/27 9:36
Keep thinking, keep coding!
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if q.val == root.val:
            return q
        if p.val == root.val:
            return p

        right = self.lowestCommonAncestor(root.right, p, q)
        left = self.lowestCommonAncestor(root.left, p, q)
        if right is not None and left is not None:
            return root
        if right is not None:
            return right
        return left
