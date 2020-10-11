# -*- coding:utf-8 -*-
"""
@author caoduanxi
@date   2020/10/9 8:58
Keep thinking, keep coding!
leetcode 142、环形链表II
获取环的入口节点，无环返回null
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None

        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast

        return None
