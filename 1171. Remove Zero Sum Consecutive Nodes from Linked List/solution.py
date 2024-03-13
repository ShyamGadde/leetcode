#
# @lc app=leetcode id=1171 lang=python3
#
# [1171] Remove Zero Sum Consecutive Nodes from Linked List
#
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/
#
# algorithms
# Medium (43.38%)
# Likes:    2917
# Dislikes: 178
# Total Accepted:    115.1K
# Total Submissions: 229.1K
# Testcase Example:  '[1,2,-3,3,1]'
#
# Given the head of a linked list, we repeatedly delete consecutive sequences
# of nodes that sum to 0 until there are no such sequences.
#
# After doing so, return the head of the final linked list.  You may return any
# such answer.
#
#
# (Note that in the examples below, all sequences are serializations of
# ListNode objects.)
#
# Example 1:
#
#
# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.
#
#
# Example 2:
#
#
# Input: head = [1,2,3,-3,4]
# Output: [1,2,4]
#
#
# Example 3:
#
#
# Input: head = [1,2,3,-3,-2]
# Output: [1]
#
#
#
# Constraints:
#
#
# The given linked list will contain between 1 and 1000 nodes.
# Each node in the linked list has -1000 <= node.val <= 1000.
#
#
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We need to do this for cases like [-1, 1] where the entire list can be removed.
        dummy = ListNode(0)
        seen = {0: dummy}
        dummy.next = head

        prefix = 0

        while head:
            prefix += head.val
            seen[prefix] = head
            head = head.next

        prefix = 0
        head = dummy

        while head:
            prefix += head.val
            head.next = seen[prefix].next
            head = head.next

        return dummy.next


# @lc code=end
