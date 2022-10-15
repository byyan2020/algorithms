#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (49.30%)
# Likes:    2864
# Dislikes: 1663
# Total Accepted:    1.1M
# Total Submissions: 2.2M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Follow up: Could you solve it without converting the integer to a string?
# 
# 
# Example 1:
# 
# 
# Input: x = 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Example 4:
# 
# 
# Input: x = -101
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        if x_str == x_str[::-1]:
            return True
        return False

        
# @lc code=end

sol = Solution()

x = -101
y = sol.isPalindrome(x)
print(y)
