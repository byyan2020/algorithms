#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (43.89%)
# Likes:    4053
# Dislikes: 86
# Total Accepted:    391.2K
# Total Submissions: 886K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n' + '5'
#
# Write an efficient algorithm that searches for a target value in an m x n
# integer matrix. The matrix has the following properties:
# 
# 
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# 
# 
# 
# Example 1:
# 
# 
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 20
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10^9 <= matix[i][j] <= 10^9
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -10^9 <= target <= 10^9
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      row = 0
      col = len(matrix[0]) - 1
      while row < len(matrix) and col >= 0:
        num = matrix[row][col]
        if num > target:
          col += -1
        elif num < target:
          row += 1
        else:
          return True
      return False
        
# @lc code=end

sol = Solution()
matrix = [[-1,3]]
target = 0
print (sol.searchMatrix(matrix, target))
