#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (47.92%)
# Likes:    5687
# Dislikes: 154
# Total Accepted:    833.1K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,2,null,3,null,3]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow up: Could you solve it both recursively and iteratively?
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     return self.isSymmetrical(root, root)
    
    # def isSymmetrical(self, root1, root2):
    #     if root1 == None and root2 == None:
    #         return True
    #     if root1 == None or root2 == None:
    #         return False
    #     if root1.val != root2.val:
    #         return False
    #     return self.isSymmetrical(root1.left, root2.right) and self.isSymmetrical(root1.right, root2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        que1, que2 = [root], [root]

        while que1:
            n = len(que1)
            # level1, level2 = [], []
            for _ in range(n):
                node1 = que1.pop(0)
                node2 = que2.pop(0)
                if node1 == None and node2 == None:
                    continue
                if node1 == None or node2 == None:
                    return False
                if node1.val != node2.val:
                    return False
                que1.append(node1.left)
                que1.append(node1.right)
                que2.append(node2.right)
                que2.append(node2.left)
        
        if que2
            return False 
        return True

        
# @lc code=end

