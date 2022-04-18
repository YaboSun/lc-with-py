#!/usr/bin/env python
# encoding: utf-8
# @Author: franky
# @Date: 2022/4/10 下午3:33


"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，
并返回其长度。如果不存在符合条件的子数组，返回 0。

示例：

输入：s = 7, nums = [2,3,1,2,4,3] 输出：2 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
"""
import sys
from typing import List


class Solution:
    # def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    #     # 暴力解法
    #     ret_len = sys.maxsize
    #     for i in range(len(nums)):
    #         tmp = nums[i]
    #         if tmp >= target:
    #             ret_len = 1
    #             break
    #         for j in range(i + 1, len(nums)):
    #             tmp = tmp + nums[j]
    #             if tmp >= target:
    #                 ret_len = min(ret_len, j - i + 1)
    #                 break
    #     return ret_len if ret_len != sys.maxsize else 0

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 滑动窗口
        i = j = 0
        tmp = 0
        ret_len = sys.maxsize
        while j < len(nums):
            tmp += nums[j]
            while tmp >= target:
                ret_len = min(ret_len, j - i + 1)
                tmp -= nums[i]
                i += 1
            j += 1

        return ret_len if ret_len != sys.maxsize else 0


if __name__ == '__main__':
    so = Solution()
    print(so.minSubArrayLen(4, [1, 4, 4]))
