from typing import Optional


# @leet start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        tmp = res

        head = head.next

        while head.next:
            if head.val == 0:
                tmp.next = ListNode()
                tmp = tmp.next

                head = head.next
                continue

            tmp.val += head.val
            head = head.next

        return res


# @leet end
