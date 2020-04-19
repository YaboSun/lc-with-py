"""
java实现

class Solution {
    public int removeDuplicates(int[] nums) {
        int len = nums.length;
        if(len <= 1) {
            return len;
        }
        int j = 0;
        for(int i = 0; i < len; i ++) {
            if(nums[i] != nums[j]) {
                nums[j + 1] = nums[i];
                j++;
            }
        }

        return j + 1;
    }
}
"""
from matplotlib.mathtext import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        newTail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                nums[newTail + 1] = nums[i]
                newTail = newTail + 1
        return newTail + 1
