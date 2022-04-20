# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
#  Related Topics 数组 双指针 排序 👍 4659 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import copy
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret_nums = []
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if nums[i] > 1:
                break
            # 去重
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                tmp_sum = nums[i] + nums[left] + nums[right]
                if tmp_sum == 0:
                    ret_nums.append([nums[i], nums[left], nums[right]])
                    while left != right and nums[left] == nums[left + 1]:  # 去重
                        left += 1
                    while left != right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 如果相等再去除重复数字之后需要同时更新2个index
                    left += 1
                    right -= 1
                elif tmp_sum < 0:
                    left += 1
                else:
                    right -= 1
        return ret_nums

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     # 双数和四数都用的hash 这题很容易也陷入hash的思考范围
    #     # 考虑用回溯来求解
    #     path = list()
    #     res = list()
    #
    #     def work(index):
    #         if len(path) > 3:
    #             return
    #         if len(path) == 3 and sum(path) == 0:
    #             res.append(copy.deepcopy(path))
    #
    #         for i in range(index, len(nums)):
    #             path.append(nums[i])
    #             work(i + 1)
    #             path.pop(-1)
    #
    #     work(0)
    #     return res


if __name__ == '__main__':
    so = Solution()
    print(so.threeSum([-1, 0, 1, 2, -1, -4]))
# leetcode submit region end(Prohibit modification and deletion)
