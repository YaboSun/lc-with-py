# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。 
# 
#  
#  如果剩余字符少于 k 个，则将剩余字符全部反转。 
#  如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abcdefg", k = 2
# 输出："bacdfeg"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "abcd", k = 2
# 输出："bacd"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 仅由小写英文组成 
#  1 <= k <= 10⁴ 
#  
#  Related Topics 双指针 字符串 👍 283 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse_str(s_list):
            left = 0
            right = len(s_list) - 1
            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            return s_list
        s_list = list(s)
        n = len(s)
        for i in range(0, n, 2 * k):
            s_list[i: i + k] = reverse_str(s_list[i: i + k])

        return "".join(s_list)
# leetcode submit region end(Prohibit modification and deletion)
