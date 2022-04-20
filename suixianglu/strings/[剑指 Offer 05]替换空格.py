# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "We are happy."
# 输出："We%20are%20happy." 
# 
#  
# 
#  限制： 
# 
#  0 <= s 的长度 <= 10000 
#  Related Topics 字符串 👍 265 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def replaceSpace(self, s: str) -> str:
        count = s.count(" ")
        s_list = list(s)
        s_list.extend([" "] * count * 2)
        left = len(s) - 1
        right = len(s_list) - 1
        while left >= 0:
            if s[left] != " ":
                s_list[right] = s[left]
                right -= 1
            else:
                s_list[right - 2: right + 1] = "%20"
                right -= 3
            left -= 1
        return "".join(s_list)
# leetcode submit region end(Prohibit modification and deletion)
