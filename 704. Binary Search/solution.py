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

        while lhs <= rhs:  # We write <= for the case where element is in the center of odd number of elements.
            mid = lhs + (rhs - lhs) // 2  # The reason for doing this just defensive programming is case the number of very large and may cause integer overflow. 
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

