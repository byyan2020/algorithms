#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (44.45%)
# Likes:    3147
# Dislikes: 157
# Total Accepted:    289.3K
# Total Submissions: 649.9K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
# 
# Example 1:
# Given tree s:
# 
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# 
# Given tree t:
# 
# 
# ⁠  4 
# ⁠ / \
# ⁠1   2
# 
# Return true, because t has the same structure and node values with a subtree
# of s.
# 
# 
# 
# Example 2:
# Given tree s:
# 
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
# 
# Given tree t:
# 
# 
# ⁠  4
# ⁠ / \
# ⁠1   2
# 
# Return false.
# 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # 对s的每一个节点，都判断t是否等于该节点的子树
        if not s: 
            return False
        if self.isMatch(s,t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isMatch(self, s, t):
        if not (s and t):
            return s is t
        return (s.val == t.val and self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right))
        

    # def isSubnode(self, s, the):
    #     # return same subnode
    #     pass

        
# @lc code=end

