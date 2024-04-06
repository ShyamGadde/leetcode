# @before-stub-for-debug-begin
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
        if not head:
            return prev

        nxt, head.next = head.next, prev
        return self.reverseList(nxt, head)


# Time complexity: O(N)
# Space complexity: O(N)

# @lc code=end
