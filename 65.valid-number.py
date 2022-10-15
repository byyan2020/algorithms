#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#
# https://leetcode.com/problems/valid-number/description/
#
# algorithms
# Hard (15.75%)
# Likes:    860
# Dislikes: 5465
# Total Accepted:    192.9K
# Total Submissions: 1.2M
# Testcase Example:  '"0"'
#
# A valid number can be split up into these components (in order):
# 
# 
# A decimal number or an integer.
# (Optional) An 'e' or 'E', followed by an integer.
# 
# 
# A decimal number can be split up into these components (in order):
# 
# 
# (Optional) A sign character (either '+' or '-').
# One of the following formats:
# 
# At least one digit, followed by a dot '.'.
# At least one digit, followed by a dot '.', followed by at least one
# digit.
# A dot '.', followed by at least one digit.
# 
# 
# 
# 
# An integer can be split up into these components (in order):
# 
# 
# (Optional) A sign character (either '+' or '-').
# At least one digit.
# 
# 
# For example, all the following are valid numbers: ["2", "0089", "-0.1",
# "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93",
# "-123.456e789"], while the following are not valid numbers: ["abc", "1a",
# "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
# 
# Given a string s, return true if s is a valid number.
# 
# 
# Example 1:
# 
# 
# Input: s = "0"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "e"
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: s = "."
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: s = ".1"
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 20
# s consists of only English letters (both uppercase and lowercase), digits
# (0-9), plus '+', minus '-', or dot '.'.
# 
# 
#
# 一个数值可被表示为a[[.b]][e|Ec]，其中a，c为有符号整数，b为无符号整数

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        n = len(s)
        i = 0
        n_digit = 0
        n_dot = 0

        # skip the whitespaces
        while i<n and s[i] == ' ':
            i += 1
        
        # check the significand
        if s[i] == '+' or s[i] == '-':
            i += 1
        
        while i<n and (s[i].isdigit() or s[i] == '.'):
            if s[i] == '.':
                n_dot += 1
            else:
                n_digit += 1
            i += 1
        
        if n_dot>1 or n_digit<1:
            return False
        
        # check if the exponent exists
        if i<n and (s[i] == 'e' or s[i] == 'E'):
            i += 1
            if i<n and (s[i] == '+' or s[i] == '-'):
                i += 1

            n_digit = 0
            while i<n and s[i].isdigit():
                n_digit += 1
                i += 1
            if n_digit < 1:
                return False
        
        # skip the trailing whitespaces
        while i<n and s[i] == ' ':
            i += 1
        
        return i == n
    
# @lc code=end

sol = Solution()
print(sol.isNumber("6+1"))