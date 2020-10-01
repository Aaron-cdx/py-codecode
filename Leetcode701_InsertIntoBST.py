# -*- coding:utf-8 -*-
"""
@author caoduanxi
@date   2020/9/30 9:25
Keep thinking, keep coding!
"""
from Leetcode235_LowestCommonAncestor import TreeNode


class Solution:
    """
    二叉搜索树树插入节点，这里判断的是当前的值大小，然后顺着当前值参与判断即可
    """

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root
