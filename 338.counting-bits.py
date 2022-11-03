#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Easy (74.39%)
# Likes:    7992
# Dislikes: 376
# Total Accepted:    686.9K
# Total Submissions: 913.3K
# Testcase Example:  '2'
#
# Given an integer n, return an array ans of length n + 1 such that for each i
# (0 <= i <= n), ans[i] is the number of 1's in the binary representation of
# i.
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 
# 
# Example 2:
# 
# 
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 10^5
# 
# 
# 
# Follow up:
# 
# 
# It is very easy to come up with a solution with a runtime of O(n log n). Can
# you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like
# __builtin_popcount in C++)?
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n + 1)]
        offset = 1
        for i in range(1, n + 1):
            if i == offset * 2:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
        
# @lc code=end

