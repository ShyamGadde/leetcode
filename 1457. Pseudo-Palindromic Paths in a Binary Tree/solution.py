#
# @lc app=leetcode id=1457 lang=python3
#
# [1457] Pseudo-Palindromic Paths in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        count = 0
        # 1 for odd, 0 for even
        freq = [0] * 10

        def dfs(node):
            if not node:
                return

            freq[node.val] ^= 1

            # Check if it's a leaf node
            if not node.left and not node.right:
                if sum(v & 1 for v in freq) <= 1:
                    nonlocal count
                    count += 1
            else:
                dfs(node.left)
                dfs(node.right)

            freq[node.val] ^= 1  # Backtrack

        dfs(root)

        return count


# @lc code=end
