#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            if p and q and p.val == q.val:
                queue.extend([(p.left, q.left), (p.right, q.right)])
            elif p or q:
                return False
        return True

# Time complexity: O(N)
# Space complexity: O(N)
        
# @lc code=end

# Using BFS
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         queue = deque([(p, q)])
#         while queue:
#             p, q = queue.popleft()
#             if p and q and p.val == q.val:
#                 queue.extend([(p.left, q.left), (p.right, q.right)])
#             elif p or q:
#                 return False
#         return True

# Time complexity: O(N)
# Space complexity: O(N)



# Recursive DFS

# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if not p and not q:
#             return True

#         if not p or not q or p.val != q.val:
#             return False

#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Time complexity: O(N)
# Space complexity: O(N)
