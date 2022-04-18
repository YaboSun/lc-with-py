#!/usr/bin/env python
# encoding: utf-8
# @Author: franky
# @Date: 2022/4/11 下午6:38
from suixianglu.linkedlist import ListNode

"""
题意：反转一个单链表。

示例: 输入: 1->2->3->4->5->NULL 输出: 5->4->3->2->1->NULL


"""


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        tmp_stack = []
        cur_node = head
        while cur_node.next is not None:
            tmp_stack.append(cur_node.val)

        ret_listnode = ListNode(val=tmp_stack.pop())
        while tmp_stack is not None:
            ret_listnode.next = ListNode(val=tmp_stack.pop())
            ret_listnode = ret_listnode.next

        return ret_listnode
