from typing import *

#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lhs, rhs = 0, len(nums) - 1

        while lhs <= rhs:  # We write <= for the case where only one element is left
            mid = lhs + (rhs - lhs) // 2   # The reason for doing this is just defensive programming i.e., is case the number is very large and may cause integer overflow. (not required in Python though)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lhs = mid + 1
            else:
                rhs = mid - 1
        return -1

# Time complexity: O(LogN)
# Space complexity: O(1)

# @lc code=end

