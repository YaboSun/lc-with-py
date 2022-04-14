# 给你一个链表，删除链表的倒数第 n 个结点，
# 并且返回链表的头结点。
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1], n = 1
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1,2], n = 1
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中结点的数目为 sz 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz 
#  
# 
#


#
#  进阶：你能尝试使用一趟扫描实现吗？ 
#  Related Topics 链表 双指针 👍 1961 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow_node = head
        fast_node = head
        pre_node = head
        while n > 0:
            fast_node = fast_node.next
            n -= 1
        if not fast_node:
            return head.next
        while fast_node is not None:
            pre_node = slow_node
            slow_node = slow_node.next
            fast_node = fast_node.next

        pre_node.next = pre_node.next.next
        return head

# leetcode submit region end(Prohibit modification and deletion)
