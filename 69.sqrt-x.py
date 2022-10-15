#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (34.70%)
# Likes:    1739
# Dislikes: 2193
# Total Accepted:    661.7K
# Total Submissions: 1.9M
# Testcase Example:  '4'
#
# Given a non-negative integer x, compute and return the square root of x.
# 
# Since the return type is an integer, the decimal digits are truncated, and
# only the integer part of the result is returned.
# 
# 
# Example 1:
# 
# 
# Input: x = 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part
# is truncated, 2 is returned.
# 
# 
# Constraints:
# 
# 
# 0 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1 :
            return x
        left = 1
        right = x-1
        while left <= right:
            mid = left + (right - left) // 2
            if x / mid > mid:
                if x / (mid + 1) < mid + 1:
                    return mid
                else:
                    left = mid + 1
            elif x / mid < mid:
                right = mid - 1
            else:
                return mid
        
# @lc code=end

