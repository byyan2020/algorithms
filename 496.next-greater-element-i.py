#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
# https://leetcode.com/problems/next-greater-element-i/description/
#
# algorithms
# Easy (71.43%)
# Likes:    5107
# Dislikes: 313
# Total Accepted:    468.8K
# Total Submissions: 656.3K
# Testcase Example:  '[4,1,2]\n[1,3,4,2]'
#
# The next greater element of some element x in an array is the first greater
# element that is to the right of x in the same array.
# 
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where
# nums1 is a subset of nums2.
# 
# For each 0 <= i < nums1.length, find the index j such that nums1[i] ==
# nums2[j] and determine the next greater element of nums2[j] in nums2. If
# there is no next greater element, then the answer for this query is -1.
# 
# Return an array ans of length nums1.length such that ans[i] is the next
# greater element as described above.
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so
# the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so
# the answer is -1.
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so
# the answer is -1.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length <= nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 10^4
# All integers in nums1 and nums2 are unique.
# All the integers of nums1 also appear in nums2.
# 
# 
# 
# Follow up: Could you find an O(nums1.length + nums2.length) solution?
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [] #(num, index)
        next_greater = collections.defaultdict(int)
        for index, num in enumerate(nums2):
            while stack and stack[-1][0] < num:
                n, i = stack.pop()
                next_greater[n] = num
            stack.append((num, index))
        
        for num, index in stack:
            next_greater[num] = -1

        res = [0] * len(nums1)
        for i in range(len(nums1)):
            res[i] = next_greater[nums1[i]]
        return res
        
# @lc code=end

