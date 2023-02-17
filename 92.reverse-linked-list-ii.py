#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (45.41%)
# Likes:    8684
# Dislikes: 389
# Total Accepted:    611.7K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Given the head of a singly linked list and two integers left and right where
# left <= right, reverse the nodes of the list from position left to position
# right, and return the reversed list.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [5], left = 1, right = 1
# Output: [5]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
# 
# 
# 
# Follow up: Could you do it in one pass?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        count = 0
        leftp = rightp = None
        pre_leftp = after_rightp = None
        cur = dummy

        # Find node before left, left node and right node
        while count <= right:
            if count == left - 1:
                pre_leftp = cur
            if count == left:
                leftp = cur
            if count == right:
                rightp = cur
            cur = cur.next
            count += 1
        after_rightp = rightp.next

        # Reverse 
        pre_leftp.next = None
        cur = leftp
        pre = after_rightp
        count = right - left + 1
        while count > 0:
            nextp = cur.next
            cur.next = pre
            pre = cur
            cur = nextp
            count -= 1

        pre_leftp.next = rightp 
        leftp.next = after_rightp
        
        return dummy.next
        
# @lc code=end

