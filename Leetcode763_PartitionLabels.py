# -*- coding:utf-8 -*-
"""
@author caoduanxi
@date   2020/10/22 9:34
Keep thinking, keep coding!
leetcode 763、划分数字区间
题目：https://leetcode-cn.com/problems/partition-labels/
"""
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        res = list()
        if S is None or len(S) == 0:
            return res
        # 构造26个初始值为0的作为
        alpha = [0] * 26
        for i, ch in enumerate(S):
            alpha[ord(ch) - ord("a")] = i

        start, end = 0, 0
        for i, ch in enumerate(S):
            end = max(end, alpha[ord(ch) - ord("a")])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.partitionLabels("ababcbacadefegdehijhklij"))
