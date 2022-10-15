#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#
# https://leetcode.com/problems/integer-break/description/
#
# algorithms
# Medium (51.08%)
# Likes:    1404
# Dislikes: 246
# Total Accepted:    123K
# Total Submissions: 240.8K
# Testcase Example:  '2'
#
# Given a positive integer n, break it into the sum of at least two positive
# integers and maximize the product of those integers. Return the maximum
# product you can get.
# 
# Example 1:
# 
# 
# 
# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# 
# 
# Example 2:
# 
# 
# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# 
# Note: You may assume that n is not less than 2 and not larger than 58.
# 
# 
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        products = [False for i in range(0, n+1)]
        products[1] = 1
        products[2] = 2
        products[3] = 3
        # if n < 4:
        for i in range(4,n+1):
            max = 0
            for j in range(1, i//2+1):
                pr = products[j] * products[i-j]      
                if pr > max:
                    max = pr
            products[i] = max
        return products[n]
          
# @lc code=end

sol = Solution()


print(sol.integerBreak(10))