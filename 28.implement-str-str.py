#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (34.96%)
# Likes:    2080
# Dislikes: 2192
# Total Accepted:    796.6K
# Total Submissions: 2.3M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# Clarification:
# 
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
# 
# 
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Example 3:
# Input: haystack = "", needle = ""
# Output: 0
# 
# 
# Constraints:
# 
# 
# 0 <= haystack.length, needle.length <= 5 * 10^4
# haystack and needle consist of only lower-case English jaracters.
# 
# 
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if not needle:
        #     return 0 
        # i = 0
        # j = 0
        # hold = 0
        # ans = -1
        # while j < len(haystack):
        #     if i < len(needle):
        #         if haystack[j] == needle[0]:
        #             hold = j
        #             i += 1
        #         elif haystack[j] == needle[i]:
        #             i += 1
        #         else:
        #             if i:
        #                 j = hold-1
        #                 i = 0


        #     else:
        #         ans = j - i
        #         break
                        
        #     j += 1

        # if len(needle) > i:
        #     return -1
        # return ans 
        h_size, n_size = len(haystack), len(needle)

        for i in range(h_size - n_size + 1):
            if haystack[i:i+p] == needle:
                return i
        return -1


        
# @lc code=end
sol = Solution()

x = "hello"
val = "ll"
y = sol.strStr(x, val)
print(y)
