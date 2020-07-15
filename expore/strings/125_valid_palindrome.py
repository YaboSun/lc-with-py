"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = filter(str.isalnum, s)
        s_fin = "".join(list(s_new)).lower()

        i, j = 0, len(s_fin) - 1
        while i <= j:
            if s_fin[i] != s_fin[j]:
                return False
            else:
                i = i + 1
                j = j - 1
        return True


if __name__ == '__main__':
    so = Solution()
    print(so.isPalindrome("A man, a plan, a canal: Panama"))
