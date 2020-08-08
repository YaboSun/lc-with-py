"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from typing import List


class Solution:
    """
    俩俩进行比较，获得当前最大值，保证每次只增加
    """

    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] = nums[i] + nums[i - 1]
        return max(nums)

    def maxSubArray2(self, nums: List[int]) -> int:
        """
        todo dp解法
        :param nums:
        :return:
        """
        length = len(nums)
        dp = [nums[0]]

        for i in range(1, length):
            if dp[i - 1] > 0:
                dp.append(dp[i - 1] + nums[i])
            else:
                dp.append(nums[i])

        ret_max = max(dp)

        return ret_max


if __name__ == '__main__':
    so = Solution()
    so.maxSubArray2([2, 3, 4, -1])
