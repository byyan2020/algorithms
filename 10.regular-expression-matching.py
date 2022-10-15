#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (27.25%)
# Likes:    5292
# Dislikes: 818
# Total Accepted:    504.4K
# Total Submissions: 1.8M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*' where: 
# 
# 
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# 
# 
# The matching should cover the entire input string (not partial).
# 
# 
# Example 1:
# 
# 
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# 
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# Example 4:
# 
# 
# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore,
# it matches "aab".
# 
# 
# Example 5:
# 
# 
# Input: s = "mississippi", p = "mis*is*p*."
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 20
# 0 <= p.length <= 30
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a
# previous valid character to match.
# 
# 
#

# @lc code=start
# 递归
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         if s == '' and p == '':
#             return True
#         if s =='' and len(p) == 2 and p[1] =='*':
#             return True
#         if s == '' and p != '':
#             return False
#         if s != '' and p == '':
#             return False

#         if len(p) >= 2 and p[1] == '*':
#             if s[0] == p[0] or (p[0] == '.' and s != ''):
#                 ans = self.isMatch(s + 1, p + 2) or self.isMatch(s + 1, p) or self.isMatch(s, p +2)
#                 return ans
#             return self.isMatch(s,p[2:])
        
#         if s[0] == p[0] or p[0] == '.':
#             return self.isMatch(s[1:], p[1:])
        
# 动态规划
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]

        dp[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] |= dp[i-1][j]
                elif p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                
        return dp[-1][-1]

# @lc code=end

s = 'abbbbbbbc'
p = 'ab*d*c'
sol = Solution()
print(sol.isMatch(s,p))     

