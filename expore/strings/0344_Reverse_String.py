"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List


# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         n = len(s)
#         i = 0
#         j = n - 1
#         while i <= j:
#             tmp = s[i]
#             s[i] = s[j]
#             s[j] = tmp
#             i = i + 1
#             j = j - 1

class Solution:

    def reverseString(self, s: List[str]) -> None:
        s = s[::-1]
        print(s)

