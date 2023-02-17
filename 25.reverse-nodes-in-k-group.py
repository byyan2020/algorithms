#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (53.88%)
# Likes:    10423
# Dislikes: 560
# Total Accepted:    658.5K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, reverse the nodes of the list k at a time,
# and return the modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes, in
# the end, should remain as it is.
# 
# You may not alter the values in the list's nodes, only nodes themselves may
# be changed.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
# 
# 
# 
# Follow-up: Can you solve the problem in O(1) extra memory space?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = cur = dummy
        count = 0

        while cur:
            # Count k nodes to perform reverse
            if count == k:
                # Disconnect tail to k group head
                tail.next = None
                # Get new head and new tail after reverse
                newhead, newtail = self.reverse(khead, cur, k)
                # Connect tail to head of reversed group
                tail.next = newhead
                # update tail and cur
                tail = newtail
                cur = newtail
                # update count to be 0
                count = 0
            # not k nodes, cur move to next and count + 1
            else:
                count += 1
                cur = cur.next
                # Record head of k group
                if count == 1:
                    khead = cur
        return dummy.next
    
    """
    Reverse first k Node
    Input old head, old tail and k, return new head and new tail
    1 -> 2 -> 3, head.val = 1, tail.val = 2, k = 2
    2 -> 1 -> 3
    """
    def reverse(self, head, tail, k):
        dummy = ListNode(0, head)
        # Important! head(1) should point to tail.next(3)
        pre = tail.next
        cur = head
        while k > 0:
            k -= 1
            nextp = cur.next
            cur.next = pre
            pre = cur
            cur = nextp
        return tail, head
        
# @lc code=end

