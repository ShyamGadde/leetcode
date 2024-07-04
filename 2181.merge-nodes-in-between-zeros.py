from typing import Optional


# @leet start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        start = head

        while start:
            sum = 0
            end = start

            while end.val != 0:
                sum += end.val
                end = end.next

            start.val = sum
            start.next = end.next

            start = start.next

        return head


# @leet end
