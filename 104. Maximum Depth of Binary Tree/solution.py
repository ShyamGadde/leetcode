#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        res = 0

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return res

# Time complexity: O(N)
# Space complexity: O(N)

# @lc code=end

# Recursive DFS
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0

# Time complexity: O(N)
# Space complexity: O(N)

# Using BFS
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         from collections import deque
#         levels = 0
#         queue = deque([root])
#         while queue:
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 if node.left:   
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             levels += 1
#         return levels

# Time complexity: O(N)
# Space complexity: O(N)

