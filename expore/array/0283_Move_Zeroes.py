"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Java解法 双指针
class Solution {
    public void moveZeroes(int[] nums) {
        int i = 1;
        for(int j = 0; j < nums.length && i < nums.length; j++) {
            if(nums[j] == 0) {
                while(nums[i] == 0 && i < nums.length - 1) {
                    i++;
                }
                swap(nums, i, j);
            }
            i++;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
