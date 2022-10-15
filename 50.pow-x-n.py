#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (30.84%)
# Likes:    2049
# Dislikes: 3557
# Total Accepted:    584.9K
# Total Submissions: 1.9M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (i.e. x^n).
# 
# 
# Example 1:
# 
# 
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: x = 2.10000, n = 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# 
# Constraints:
# 
# 
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# -10^4 <= x^n <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0.0:
            return 1
        if n < 0.0:
            if x == 0.0:
                return False
            return 1/self.UnsignedPower(x, -n)
        return self.UnsignedPower(x,n)

    def UnsignedPower(self, base, exp):
        if exp == 0.0:
            return 1
        if exp == 1.0:
            return base
        ans = self.UnsignedPower(base, exp>>1) 
        ans = ans*ans
        if exp & 0x1 == 1:
            ans = ans * base
        return ans
        
        
# @lc code=end
mySol = Solution()
print(mySol.myPow(2.00000, -2))
