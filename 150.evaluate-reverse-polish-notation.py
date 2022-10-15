#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (37.40%)
# Likes:    1366
# Dislikes: 503
# Total Accepted:    261.3K
# Total Submissions: 696K
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
# 
# Note:
# 
# 
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would
# always evaluate to a result and there won't be any divide by zero
# operation.
# 
# 
# Example 1:
# 
# 
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# 
# Example 2:
# 
# 
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# 
# 
# Example 3:
# 
# 
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
# ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
#
from typing import List

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0

        for ch in tokens:
            if ch not in '*-+/':
                stack.append(int(ch))
            else:
                r, l = stack.pop(), stack.pop()
                if ch == '+':
                    ans = l + r
                elif ch == '-':
                    ans = l - r
                elif ch == '*':
                    ans = l * r
                else:
                    ans = int(float(l)/r)

                stack.append(ans)
            
        return stack.pop()
  
# @lc code=end

sol = Solution()

x = ["4", "13", "5", "/", "+"]
y = sol.evalRPN(x)
print(y)