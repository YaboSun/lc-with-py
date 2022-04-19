# 给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
# 解释：[4,9] 也是可通过的
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums1.length, nums2.length <= 1000 
#  0 <= nums1[i], nums2[i] <= 1000 
#  
#  Related Topics 数组 哈希表 双指针 二分查找 排序 👍 528 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     # 暴力解法
    #     ret_nums = set()
    #     for i in range(len(nums1)):
    #         for j in range(len(nums2)):
    #             if nums1[i] == nums2[j]:
    #                 ret_nums.add(nums1[i])
    #     return list(ret_nums)

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# leetcode submit region end(Prohibit modification and deletion)
