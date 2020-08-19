"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = max(nums)
        new_nums = [None] * (n + 1)
        for i in nums:
            new_nums[i] = i

        maxret = 0
        for i in range(len(new_nums)):
            if new_nums[i] is None:
                return i
            else:
                maxret = i + 1

        return maxret