#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (35.92%)
# Likes:    3444
# Dislikes: 2063
# Total Accepted:    901K
# Total Submissions: 2.5M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# 
# Example 1:
# 
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # test_str = strs[0]
        # test_strs = []
        # for n in range(len(test_str)):
        #     test_s = ''
        #     for char in test_str[n:]:
        #         test_s += char
        #         test_strs.append(test_s) 
        # flag = 0
        # for prefix in test_strs:
        #     for s in strs:
        #         if prefix not in s:
        #             flag = 1
        #             break
        #     if flag == 0:
        #         return prefix
            
        # return "\"\""
        if strs == []:
            return ''
        length, count = len(strs[0]), len(strs)
        # prefix = ''
        # flag = 0
        for i in range(length):
            for j in range(1, count):
                if len(strs[j]) == i or strs[0][i] != strs[j][i]:
        #             flag = 1
        #             break
        #     if flag == 0:   # 遍历了第一纵列，如何写遍历字母都相等的判断条件
        #         prefix += strs[0][i]
        # return prefix   
                    return strs[0][:i]
        return strs[0]


sol = Solution()    

x = ["f"]
y = sol.longestCommonPrefix(x)
print(y)
        
# @lc code=end

