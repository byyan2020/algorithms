#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (64.50%)
# Likes:    6002
# Dislikes: 117
# Total Accepted:    1.2M
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node_cur = head
        node_behind = None
        while node_cur != None:
            # 1   2   3  
            node_ahead = node_cur.next
            node_cur.next = node_behind
            node_behind = node_cur
            node_cur = node_ahead
            
        return node_behind


# @lc code=end

