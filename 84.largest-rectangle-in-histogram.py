#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (40.93%)
# Likes:    12870
# Dislikes: 182
# Total Accepted:    615.6K
# Total Submissions: 1.5M
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in
# the histogram.
# 
# 
# Example 1:
# 
# 
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10
# units.
# 
# 
# Example 2:
# 
# 
# Input: heights = [2,4]
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= heights.length <= 10^5
# 0 <= heights[i] <= 10^4
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (heihgt, index)

        for cur_index, cur_height in enumerate(heights):
            start = cur_index
            while stack and stack[-1][0] > cur_height:
                pop_height, pop_index = stack.pop()
                max_area = max(max_area, (cur_index - pop_index) * pop_height)
                start = pop_index
            stack.append((cur_height, start))
        
        for cur_height, cur_index in stack:
            max_area = max(max_area, (len(heights) - cur_index) * cur_height)
        
        return max_area
        
# @lc code=end

