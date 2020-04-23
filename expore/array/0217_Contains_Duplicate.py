"""
Java Solution:
最简单的暴力法就是双指针直接判断，但是时间复杂度肯定超了，稍微优化：
先进行排序 然后直接前后对比，这里选择从索引1开始考虑到nums只有一个数的情况
或者可以写成先判断长度，然后再从0开始进行判断
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for(int i = 1; i < nums.length; i++) {
            if(nums[i] == nums[i - 1]) {
                return true;
            }
        }
        return false;
    }
}

还有一种是利用Java中HashSet没有重复的特性直接添加，添加之前判断元素是否已经存在
class Solution {
    public boolean containsDuplicate(int[] nums) {
        final Set<Integer> set = new HashSet<Integer>();
        for(int num : nums) {
            if(set.contains(num)) {
                return true;
            }
            set.add(num);
        }
        return false;
    }
}
"""


# 参考第一种解法
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) <= 1:
            return False
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


# 利用set特性
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nset = set(nums)
        if len(nset) < len(nums):
            return True
        return False
