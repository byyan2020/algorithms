#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (51.55%)
# Likes:    5188
# Dislikes: 612
# Total Accepted:    437.7K
# Total Submissions: 844.8K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given the head of a linked list and a value x, partition it such that all
# nodes less than x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [2,1], x = 2
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_dummy = smaller_list = ListNode()
        greater_dummy = greater_list = ListNode()

        cur = head

        while cur:
            if cur.val >= x :
                greater_list.next = cur 
                greater_list = greater_list.next
            else:
                smaller_list.next = cur 
                smaller_list = smaller_list.next 
            cur = cur.next

        smaller_list.next = greater_dummy.next
        greater_list.next = None 

        return smaller_dummy.next     
# @lc code=end

