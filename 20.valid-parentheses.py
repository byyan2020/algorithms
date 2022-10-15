#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (39.46%)
# Likes:    6318
# Dislikes: 261
# Total Accepted:    1.2M
# Total Submissions: 3.1M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: s = "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: s = "{[]}"
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

# @lc code=start

# 遍历str
# 1.左括号，存在list里
# 2.右括号，与list里的左括号配对
#     ——可以配对
#         删除掉list里的左括号
#     ——不可以配对，return false
# 遍历完成，如list为空，则return true，else return false

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            '[':']',
            '{':'}',
            '(':')'
        }

        stack = [] # list()
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            else:
                if len(stack) != 0 and pairs[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
        # if stack == []:
        return len(stack) == 0
            # return True
        # return False
# @lc code=end

sol = Solution()    

x ="{}]"
y = sol.isValid(x)
print(y)

                

