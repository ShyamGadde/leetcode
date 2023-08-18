#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return -1

            # Calculate height of left and right node
            left, right = dfs(node.left), dfs(node.right)
            self.diameter = max(self.diameter, left + right + 2)
            return max(left, right) + 1

        dfs(root)

        return self.diameter


# @lc code=end
