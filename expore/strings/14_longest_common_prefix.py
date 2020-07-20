"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        ret = []
        for i in range(len(shortest)):
            for j in range(len(strs)):
                if shortest[i] != strs[j][i]:
                    return ''.join(ret)
            ret.append(shortest[i])

        return ''.join(ret)


if __name__ == '__main__':
    str_list = ["flower", "flow", "flight"]
    so = Solution()
    print(so.longestCommonPrefix(str_list))
