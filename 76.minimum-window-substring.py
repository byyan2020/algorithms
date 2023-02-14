#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (40.76%)
# Likes:    13922
# Dislikes: 606
# Total Accepted:    945.9K
# Total Submissions: 2.3M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty
# string "".
# 
# The testcases will be generated such that the answer is unique.
# 
# 
# Example 1:
# 
# 
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
# 
# 
# Example 2:
# 
# 
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# 
# 
# Example 3:
# 
# 
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
# 
# 
# 
# Constraints:
# 
# 
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
# 
# 
# 
# Follow up: Could you find an algorithm that runs in O(m + n) time?
# 
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap = collections.defaultdict(int)
        for char in t:
            hashmap[char] += 1
        start, end = 0, 0
        counter = len(t)
        res = ''  
        min_len = float('inf')

        while end < len(s):
            if hashmap[s[end]] > 0:
                counter -= 1
            hashmap[s[end]] -= 1
            end += 1
            while counter <= 0:
                if end - start < min_len:
                    res = s[start : end]
                    min_len = end - start
                if hashmap[s[start]] == 0: 
                    counter += 1
                hashmap[s[start]] += 1
                start += 1
        return res
        
# @lc code=end

