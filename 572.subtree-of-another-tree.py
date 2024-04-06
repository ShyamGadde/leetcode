#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def same_tree(self, p, q):
        if p and q:
            return (
                p.val == q.val
                and self.same_tree(p.left, q.left)
                and self.same_tree(p.right, q.right)
            )
        return p is q  # Check for null node


# @lc code=end
