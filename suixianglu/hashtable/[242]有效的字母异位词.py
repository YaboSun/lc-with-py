# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。 
# 
#  注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "rat", t = "car"
# 输出: false 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length, t.length <= 5 * 10⁴ 
#  s 和 t 仅包含小写字母 
#  
# 
#  
# 
#  进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
#  Related Topics 哈希表 字符串 排序 👍 555 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter, defaultdict


class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     record = [0] * 26
    #     for c in s:
    #         record[ord(c) - ord('a')] += 1
    #     for c in t:
    #         record[ord(c) - ord('a')] -= 1
    #
    #     for i in range(len(record)):
    #         if record[i] != 0:
    #             return False
    #     return True
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     for c in range(ord('a'), ord('z') + 1):
    #         if s.count(chr(c)) != t.count(chr(c)):
    #             return False
    #
    #     return True

    # def isAnagram(self, s: str, t: str) -> bool:
    #     return Counter(s) == Counter(t)
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for c in s:
            s_dict[c] += 1
        for c in t:
            t_dict[c] += 1

        return s_dict == t_dict
# leetcode submit region end(Prohibit modification and deletion)
