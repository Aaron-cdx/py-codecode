# -*- coding:utf-8 -*-
"""
@author caoduanxi
@date   2020/10/21 10:22
Keep thinking, keep coding!
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name) - 1
        t = len(typed) - 1
        while t >= 0:
            if n >= 0 and name[n] == typed[t]:
                n -= 1
                t -= 1
            elif t + 1 < len(typed) and typed[t] == typed[t + 1]:
                t -= 1
            else:
                return False
        return n == -1
