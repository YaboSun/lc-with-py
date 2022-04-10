#!/usr/bin/env python
# encoding: utf-8
# @Author: franky
# @Date: 2022/4/8 下午2:37


"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

示例 1： 输入：nums = [-4,-1,0,3,10] 输出：[0,1,9,16,100] 解释：平方后，数组变为 [16,1,0,9,100]，排序后，数组变为 [0,1,9,16,100]

示例 2： 输入：nums = [-7,-3,2,3,11] 输出：[4,9,9,49,121]
"""
from typing import List


class Solution:
    # 暴力解法
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     for i in range(len(nums)):
    #         nums[i] = nums[i] ** 2
    #
    #     return sorted(nums)
    #
    # # 双指针，开辟新数组空间存储
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     ret_nums = [None] * len(nums)
    #     left_idx, right_idx = 0, len(nums) - 1
    #     tmp = right_idx
    #     while left_idx <= right_idx:
    #         left = nums[left_idx] ** 2
    #         right = nums[right_idx] ** 2
    #         if left < right:
    #             ret_nums[tmp] = right
    #             right_idx = right_idx - 1
    #         else:
    #             ret_nums[tmp] = left
    #             left_idx = left_idx + 1
    #         tmp = tmp - 1
    #
    #     return ret_nums

    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 可以利用一下非递减的特性 统计小于0的个数 然后拆分为三段
        # 有点繁琐
        a = 0
        length = len(nums)
        while a < length and nums[a] < 0:
            a += 1

        left = [-e for e in nums[:a][::-1]]
        min1 = nums[0]
        b = a
        if min1 < 0:
            while b < length and nums[b] < -min1:
                b += 1
        right = nums[b:]

        left.extend(nums[a:b])
        return [e**2 for e in sorted(left)] + [e**2 for e in right]


if __name__ == '__main__':
    so = Solution()
    print(so.sortedSquares([-7, -3, 2, 3, 11]))
