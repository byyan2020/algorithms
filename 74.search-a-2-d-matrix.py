#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (47.14%)
# Likes:    10750
# Dislikes: 323
# Total Accepted:    1.1M
# Total Submissions: 2.3M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# Write an efficient algorithm that searches for a value target in an m x n
# integer matrix matrix. This matrix has the following properties:
# 
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        row = 0
        start_row, end_row = 0, len(matrix)-1
        while start_row + 1 < end_row:
            mid_row = (start_row + end_row) // 2
            if matrix[mid_row][0] > target:
                end_row = mid_row
            elif matrix[mid_row][0] < target:
                start_row = mid_row
            else:
                end_row = mid_row
        
        if matrix[end_row][0] > target >= matrix[start_row][0]:
            row = start_row
        else:
            row = end_row

        start_col, end_col = 0, len(matrix[0])-1
        while start_col + 1 < end_col:
            mid_col = (start_col + end_col) // 2
            if matrix[row][mid_col] > target:
                end_col = mid_col
            else:
                start_col = mid_col

        print(row, start_col, end_col)
        if matrix[row][start_col] == target:
            return True
        if matrix[row][end_col] == target:
            return True
        return False

        
# @lc code=end

