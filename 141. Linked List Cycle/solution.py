#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        while head:
            if head in visited_nodes:
                return True
            visited_nodes.add(head)
            head = head.next
        return False

# Time complexity: O(N)
# Space complexity: O(N)

# @lc code=end

