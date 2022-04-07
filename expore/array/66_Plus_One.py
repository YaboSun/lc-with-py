"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
# 开始思路有问题，就是直接将数组转化为整数并进行+1操作，然后再转化为整型数组
# 思路是没有问题，但是实现过程还是对语法不太熟悉
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i] # 这里需要注意是加元素，而不是i
        return [int(j) for j in str(num + 1)]
