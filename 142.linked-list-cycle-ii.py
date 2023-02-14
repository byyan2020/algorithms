#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (39.40%)
# Likes:    3770
# Dislikes: 283
# Total Accepted:    416.9K
# Total Submissions: 1.1M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
# 
# There is a cycle in a linked list if there is some node in the list that can
# be reached again by continuously following the next pointer. Internally, pos
# is used to denote the index of the node that tail's next pointer is connected
# to. Note that pos is not passed as a parameter.
# 
# Notice that you should not modify the linked list.
# 
# 
# Example 1:
# 
# 
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
# 
# 
# Example 3:
# 
# 
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
# 
# 
# 
# Constraints:
# 
# 
# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.
# 
# 
# 
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
# 
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 第一步先确定链表中是否有环：两个指针，一个走一步，一个走两步，如果两个指针对应的节点是相同的，则列表中有环，如果快指针走到了末尾两个指针都没有相遇，则没有环
# 第二步求出环中有n个节点：从第一步中两个指针相遇的那个节点开始，走一步记一个数，当遍历的节点等于自身时，则可求出环的个数
# 第三步找环的入口节点：维护两个节点，相距n步，当两个节点相同时，则该节点为入口
# 1，2，3，4，5，6 
# @lc code=start

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow, fast = head, head

        # Find if there is a circle
        # If the circle exsit, slow and fast will meet
        while True:
            # If there is a circle
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        # Find the entrance
        catch = head
        while catch != slow:
            catch = catch.next
            slow = slow.next

        return catch
              
            

        
# @lc code=end

