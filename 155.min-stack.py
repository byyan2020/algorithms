#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (45.79%)
# Likes:    4388
# Dislikes: 409
# Total Accepted:    655K
# Total Submissions: 1.4M
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
  # '[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# Output
# [null,null,null,null,-3,null,0,-2]
# 
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
# 
# 
# 
# Constraints:
# 
# 
# Methods pop, top and getMin operations will always be called on non-empty
# stacks.
# 
# 
#

# @lc code=start
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, num):
        self.stack.append(num)
        if not self.min_stack or self.min_stack[-1] > num:
            self.min_stack.append(num)

    def pop(self):
        num = self.stack.pop()
        if num == self.min_stack[-1]:
            self.min_stack.pop()
        return num

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

