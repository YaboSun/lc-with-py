"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch = []
        sets = set(s)
        for i in sets:
            if s.count(i) == 1:
                ch.append(s.index(i))
        if len(ch) > 0:
            return min(ch)
        else:
            return -1

if __name__ == '__main__':
    so = Solution()
    print(so.firstUniqChar("loveleetcode"))
