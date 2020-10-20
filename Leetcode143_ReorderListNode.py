# -*- coding:utf-8 -*-
"""
@author caoduanxi
@date   2020/10/20 8:56
Keep thinking, keep coding!
"""
from Leetcode142_CycleListNodeII import ListNode

# leetcode143-重排链表
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        fast = slow.next
        slow.next = None
        slow = head
        f = self.reverseList(fast)
        while slow and f:
            sTemp = slow.next
            fTemp = f.next
            slow.next = f
            f.next = sTemp
            slow = sTemp
            f = fTemp

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        node = self.reorderList(head.next)
        head.next.next = head
        head.next = None
        return node
