"""
暴力解决，时间复杂度kn，思路很简单就是直接通过一步一步整体移动
class Solution {
    public void rotate(int[] nums, int k) {
        int len = nums.length;
        if(len <= 1) {
            return;
        }
        for(int i = 0; i  < k; i++) {
            int tmp = nums[len - 1];
            for(int j = len - 2; j >= 0; j--) {
                nums[j + 1] = nums[j];
            }
            nums[0] = tmp;
        }
    }
}
最优解：将数组先整体进行reverse，然后以k为界分别翻转，思路也比较简单
class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }

    public void reverse(int[] nums, int start, int end) {
        while(start < end) {
            int tmp = nums[start];
            nums[start] = nums[end];
            nums[end] = tmp;
            start++;
            end--;
        }
    }
}
"""
from matplotlib.mathtext import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start = start + 1
            end = end - 1


"""
这个感觉用Python高级特性实现拼接有点简单
"""


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]
