"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         i = 0
#         j = 1
#         ret = []
#         while i < len(nums):
#             if nums[i] + nums[j] == target:
#                 ret.append(i)
#                 ret.append(j)
#                 return ret
#
#             elif j < len(nums) - 1:
#                 j = j + 1
#
#             else:
#                 i = i + 1
#                 j = i + 1
#
#         return ret


# vote最多solution

class Solution:
    def twoSum(self, nums: list, target: int) -> list:

        buffer_diict = {}
        for i in range(len(nums)):
            if nums[i] in buffer_diict:
                return [buffer_diict[nums[i]], i]
            else:
                buffer_diict[target - nums[i]] = i


if __name__ == '__main__':
    solution = Solution()
    solution.twoSum([])
