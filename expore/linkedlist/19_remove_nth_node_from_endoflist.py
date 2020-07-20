"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         node_len = 0
#         # 计算链表长度
#         while head is not None:
#             node_len = node_len + 1
#             head = head.next
#         del_index = node_len - n
#         del_node = head
#         while del_index > 0:
#             del_node = del_node.next
#             del_index = del_index - 1
#         del_node.val = del_node.next.val
#         del_node.next = del_node.next.next
#
#         return head
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
