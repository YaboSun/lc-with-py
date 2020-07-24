"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
"""


# Definition for singly-linked list.
# O(n) O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 找到链表中点
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 反转链表
        # TODO
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt

        # 比较前半部分和后半部分的值
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
