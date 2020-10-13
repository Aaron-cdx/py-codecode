# -*- coding:utf-8 -*-
"""
@author caoduanxi
@date   2020/10/13 9:17
Keep thinking, keep coding!
 * leetcode 24、两两交换链表中的节点
 * 即将链表中的节点两两交换
 * 1->2->3->4 ==> 2->1->4->3
"""
from Leetcode142_CycleListNodeII import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        # 这是递归的方法
        # node = head.next
        # head.next = self.swapPairs(node.next)
        # node.next = head
        # return node

        # 不使用递归
        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode
        a = pre.next
        b = a.next
        while b is not None:
            temp = b.next
            b.next = a
            a.next = temp
            pre.next = b
            if temp is None:
                break
            pre = a
            a = a.next
            b = a.next
        return dummyNode.next
