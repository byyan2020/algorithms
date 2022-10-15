#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (36.43%)
# Likes:    5059
# Dislikes: 221
# Total Accepted:    595.4K
# Total Submissions: 1.6M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells,
# where "adjacent" cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# 
# Example 1:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n = board[i].length
# 1 <= m, n <= 200
# 1 <= word.length <= 10^3
# board and word consists only of lowercase and uppercase English letters.
# 
# 
#
from typing import List

# @lc code=start

class Solution:
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                # if visited[i][j] or board[i][j] != word[0]:
                #     continue
                # visited[i][j] = True
                if self.dfs(board, i, j, word, visited):
                    return True
                # visited[i][j] = False
        return False

    def dfs(self, board, i, j, word, visited):
        if len(word) == 0:
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return False

        if visited[i][j] or board[i][j] != word[0]:
            return False
        visited[i][j] = True

        for d in self.dirs:
            # next_i = i + direct[0]
            # next_j = j + direct[1]

            # if visited[next_i][next_j]:
            #     continue

            if self.dfs(board, i+d[0], j+d[1], word[1:], visited):
                return True
        
        visited[i][j] = False
                
        return False

        
# @lc code=end

sol = Solution()

board = [["a","a"]]
word = "aaa"

print(sol.exist(board, word))