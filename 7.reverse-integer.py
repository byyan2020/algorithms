#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.82%)
# Likes:    4107
# Dislikes: 6358
# Total Accepted:    1.3M
# Total Submissions: 5.2M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Note:
# Assume we are dealing with an environment that could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
# 
# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21
# Example 4:
# Input: x = 0
# Output: 0
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x < -2**31 or x > 2**31 - 1:
            return 0
        
        sign = 1
        if x < 0:
            x = -x
            sign = -1

        y = 0
        while x != 0:
            y = y*10 + x%10
            x = x//10
        
        y = y*sign
        if y < -2**31 or y > 2**31 - 1:
            return 0
        return y

        
# @lc code=end

sol = Solution()

x = 1534236469
y = sol.reverse(x)
print(y)