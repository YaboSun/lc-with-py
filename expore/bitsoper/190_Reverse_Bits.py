"""
Reverse bits of a given 32 bits unsigned integer.



Example 1:

Input: 0000 0010 1001 0100 0001 1110 1001 1100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
"""


class Solution:
    def __init__(self):
        pass

    def reverse_bits(self, n: int) -> int:
        ret = 0
        for i in range(16):
            right_bit = n >> i & 1
            left_bit = n >> (31 - i) & 1
            ret = ret | right_bit << (31 - i)
            ret = ret | left_bit << i

        return ret
