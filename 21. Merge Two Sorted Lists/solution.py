#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2

        ptr1, ptr2 = list1, list2

        if ptr1.val < ptr2.val:
            merged_list = ptr1
            ptr1 = ptr1.next
        else:
            merged_list = ptr2
            ptr2 = ptr2.next

        tail = merged_list

        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                tail.next = ptr1
                ptr1 = ptr1.next
            else:
                tail.next = ptr2
                ptr2 = ptr2.next

            tail = tail.next

        tail.next = ptr1 or ptr2
        
        return merged_list
        
# @lc code=end

