"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""


class Solution(object):

    # TODO 没太搞懂
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = (x > 0) - (x < 0)
        r = int(str(x * s)[::-1])
        return s * r * (r < 2 ** 31)


if __name__ == '__main__':
    so = Solution()
    print(so.reverse(321))
