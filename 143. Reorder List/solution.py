#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (55.58%)
# Likes:    10482
# Dislikes: 371
# Total Accepted:    878.4K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,4]'
#
# You are given the head of a singly linked-list. The list can be represented
# as:
#
#
# L0 → L1 → … → Ln - 1 → Ln
#
#
# Reorder the list to be on the following form:
#
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
#
# You may not modify the values in the list's nodes. Only nodes themselves may
# be changed.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Merge the two halves
        first, second = head, prev
        # NOTE: The first half is always longer than the second half
        # We loop until second.next is None because at this point, the last node
        # of the first half is already pointing to the last node of the second
        # half. This indicates that all nodes have been correctly reordered and
        # no further weaving of the two halves is needed.
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next


# @lc code=end
