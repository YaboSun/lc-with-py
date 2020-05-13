"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        ptr1 = 0
        ptr2 = 0
        # 这里更新以后还需要重新引用？
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] < nums2[ptr2]:
                ptr1 = ptr1 + 1
            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 = ptr2 + 1
            else:
                res.append(nums1[ptr1])
                ptr1 = ptr1 + 1
                ptr2 = ptr2 + 1
        return res