#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#
# https://leetcode.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (44.21%)
# Likes:    533
# Dislikes: 1965
# Total Accepted:    183.1K
# Total Submissions: 412.2K
# Testcase Example:  '10\n6'
#
# We are playing the Guess Game. The game is as follows:
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I will tell you whether the number I picked is
# higher or lower than your guess.
# 
# You call a pre-defined API int guess(int num), which returns 3 possible
# results:
# 
# 
# -1: The number I picked is lower than your guess (i.e. pick < num).
# 1: The number I picked is higher than your guess (i.e. pick > num).
# 0: The number I picked is equal to your guess (i.e. pick == num).
# 
# 
# Return the number that I picked.
# 
# 
# Example 1:
# Input: n = 10, pick = 6
# Output: 6
# Example 2:
# Input: n = 1, pick = 1
# Output: 1
# Example 3:
# Input: n = 2, pick = 1
# Output: 1
# Example 4:
# Input: n = 2, pick = 2
# Output: 2
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2^31 - 1
# 1 <= pick <= n
# 
# 
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + ((right - left) >> 1)
            if guess(mid) == -1:
                right = mid - 1
            elif guess(mid) == 1:
                left = mid + 1
            else:
                return mid
        return False
        
# @lc code=end

