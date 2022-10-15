#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (34.82%)
# Likes:    10288
# Dislikes: 2552
# Total Accepted:    1.7M
# Total Submissions: 4.9M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# 
# Example 2:
# 
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
# 
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            num = 0
            if l1:
                num += l1.val
            if l2:
                num += l2.val
            num += carry
            # num = l1.val + l2.val + carry
            cur.next = ListNode(num%10)
            carry = num // 10

            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next
            cur = cur.next
        
        # if l1:
        #     while l1:
        #         num = carry + l1.val
        #         cur.next = ListNode(num % 10)
        #         carry = num // 10

        #         l1 = l1.next 
        #         cur = cur.next    
        # else:
        #     while l2:
        #         num = carry + l2.val
        #         cur.next = ListNode(num % 10)
        #         carry = num // 10

        #         l2 = l2.next 
        #         cur = cur.next   

        # if carry:
        #     cur.next = ListNode(carry)

        return dummy.next
        
# @lc code=end

sol = Solution()    
num1 = [9,9,9,9,9,9,9]
num2 = [9,9,9,9]

l1 = ListNode(-1)
cur = l1
for num in num1:
    cur.next = ListNode(num)
    cur = cur.next

l2 = ListNode(-1)
cur = l2
for num in num2:
    cur.next = ListNode(num)
    cur = cur.next

l3 = sol.addTwoNumbers(l1.next, l2.next)

num3 = []
while l3:
    num3.append(l3.val)
    l3 = l3.next
print(num3)


