#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (50.90%)
# Likes:    4555
# Dislikes: 117
# Total Accepted:    444.5K
# Total Submissions: 867K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# 
# Return the following binary tree:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
#
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        def ConstructCore(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None

            preorder_root = preorder_left
            inorder_root = index[preorder[preorder_root]]
            root = TreeNode(preorder[preorder_root])

            size_l = inorder_root - inorder_left

            root.left = ConstructCore(preorder_left+1, preorder_left+size_l, inorder_left, inorder_root-1 )

            root.right = ConstructCore(preorder_left + size_l + 1, preorder_right, inorder_root + 1, inorder_right)

            return root

        n = len(preorder)
        index = {element: i for i, element in enumerate(inorder)}
        return ConstructCore(0, n-1, 0, n-1)


# @lc code=end

