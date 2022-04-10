#!/usr/bin/env python
# encoding: utf-8
# @Author: franky
# @Date: 2022/4/10 下午6:59

"""
题意：删除链表中等于给定值 val 的所有节点。

示例 1：
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]

示例 2：
输入：head = [], val = 1
输出：[]

示例 3：
输入：head = [7,7,7,7], val = 7
输出：[]
"""
from suixianlu.linkedlist import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(next=head)  # 虚拟节点使用
        cur_node = dummy_head
        while cur_node.next is not None:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        return dummy_head.next
