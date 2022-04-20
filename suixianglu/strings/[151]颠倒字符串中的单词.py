# 给你一个字符串 s ，颠倒字符串中 单词 的顺序。 
# 
#  单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。 
# 
#  返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。 
# 
#  注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "the sky is blue"
# 输出："blue is sky the"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "  hello world  "
# 输出："world hello"
# 解释：颠倒后的字符串中不能存在前导空格和尾随空格。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "a good   example"
# 输出："example good a"
# 解释：如果两个单词间有多余的空格，颠倒后的字符串需要将单词间的空格减少到仅有一个。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 包含英文大小写字母、数字和空格 ' ' 
#  s 中 至少存在一个 单词 
#  
# 
#  
#  
# 
#  
# 
#  进阶：如果字符串在你使用的编程语言中是一种可变数据类型，请尝试使用 O(1) 额外空间复杂度的 原地 解法。 
#  Related Topics 双指针 字符串 👍 521 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseWords(self, s: str) -> str:
        # 先反转字符串，再反转单词
        s = " ".join(s.split())
        s_list = list(s)

        def reverse_(tmp_list):
            left = 0
            right = len(tmp_list) - 1
            while left < right:
                tmp_list[left], tmp_list[right] = tmp_list[right], tmp_list[left]
                left += 1
                right -= 1
            return tmp_list

        reverse_(s_list)
        left = 0
        for i in range(len(s_list) + 1):
            if i == len(s_list) or s_list[i] == " ":
                s_list[left: i] = reverse_(s_list[left: i])
                left = i + 1
        return "".join(s_list)

# leetcode submit region end(Prohibit modification and deletion)
