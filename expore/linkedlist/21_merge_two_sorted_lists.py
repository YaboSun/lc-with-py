"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        迭代解法
        :param l1:
        :param l2:
        :return:
        """
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # 如果最后一个是l1就将cur赋值给l1否则给l2
        cur.next = l1 or l2
        # 这个dummy用于虚拟的头节点
        return dummy.next

    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        递归解法
        :param l1:
        :param l2:
        :return:
        """
