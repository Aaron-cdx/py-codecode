# -*- coding:utf-8 -*-
"""
@author caoduanxi
@date   2020/10/11 9:32
Keep thinking, keep coding!
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        s = sum(nums)
        if s % 2 != 0:
            return False
        # 初步遍历,初始化
        target = s // 2
        dp = [False for i in range(target + 1)]
        dp[0] = True
        for i in range(0, len(nums)):
            # for j in range(target, -1, -1):
            #     if j - nums[i] >= 0:
            # 这里可以使用以下来代替 range(a,b,c) => 表示起始值是a,需要大于b,步长为c
            for j in range(target, nums[i] - 1, -1):
                dp[j] = dp[j] | dp[j - nums[i]]

        return dp[target]


if __name__ == '__main__':
    solution = Solution()
    print(solution.canPartition([1, 1]))
    # for j in range(10, -1, -2):
    #     print(j)
