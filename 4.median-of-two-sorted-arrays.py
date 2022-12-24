#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (35.48%)
# Likes:    21196
# Dislikes: 2386
# Total Accepted:    1.7M
# Total Submissions: 4.8M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
# 
# The overall run time complexity should be O(log (m+n)).
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# 
# 
# 
# Constraints:
# 
# 
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(nums1) > len(nums2):
            list1 = nums2
            list2 = nums1
        else:
            list1 = nums1
            list2 = nums2
        start, end = 0, len(list1) - 1
        while True:
            mid1 = (start + end) // 2
            mid2 = half - mid1 - 2

            left1 = list1[mid1] if mid1 >= 0 else float("-inf")
            right1 = list1[mid1 + 1] if mid1 + 1 < len(list1) else float('inf')
            left2 = list2[mid2] if mid2 >= 0 else float('-inf')
            right2 = list2[mid2 + 1] if mid2 + 1 < len(list2) else float('inf')

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 1:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                end = mid1 - 1
            else:
                start = mid1 + 1
        
# @lc code=end

