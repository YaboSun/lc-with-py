#!/usr/bin/env python
# encoding: utf-8
# @Author: franky
# @Date: 2022/4/10 下午5:03


"""
给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3 输出: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret_list = [[0] * n for _ in range(n)]  # 构建数组
        start_x = start_y = 0  # 起始循环点
        loop_num = n // 2  # 总共循环次数
        count = 1  # 计数

        for loop in range(1, loop_num + 1):
            for i in range(start_y, n - loop):  # 定义第一层
                ret_list[start_x][i] = count
                count += 1

            for i in range(start_y, n - loop):  # 定义第二列
                ret_list[i][n - loop] = count
                count += 1

            for i in range(n - loop, start_x, -1):  # 定义第三层
                ret_list[n - loop][i] = count
                count += 1

            for i in range(n - loop, start_y, -1):  # 定义第四列
                ret_list[i][start_y] = count
                count += 1
            start_x += 1
            start_y += 1

        if n % 2 != 0:
            ret_list[loop_num][loop_num] = n ** 2

        return ret_list


if __name__ == '__main__':
    so = Solution()
    print(so.generateMatrix(5))
