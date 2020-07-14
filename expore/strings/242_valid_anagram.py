"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_list, t_list = list(s), list(t)
        s_list.sort()
        t_list.sort()
        for i in range(len(t)):
            if s_list[i] != t_list[i]:
                return False
        return True


if __name__ == '__main__':
    so = Solution()

    print(so.isAnagram("anagram",
                       "nagaram"))
