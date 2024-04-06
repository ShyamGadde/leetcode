#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (42.96%)
# Likes:    3282
# Dislikes: 237
# Total Accepted:    282K
# Total Submissions: 648.5K
# Testcase Example:  '5\n7'
#
# Given two integers left and right that represent the range [left, right],
# return the bitwise AND of all numbers in this range, inclusive.
#
#
# Example 1:
#
#
# Input: left = 5, right = 7
# Output: 4
#
#
# Example 2:
#
#
# Input: left = 0, right = 0
# Output: 0
#
#
# Example 3:
#
#
# Input: left = 1, right = 2147483647
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= left <= right <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Find the longest common prefix of left and right,
        # because those are the only bits that will be the same after AND
        # When left < right, there is at least one bit that is different
        while left < right:
            right &= right - 1  # Remove the last set bit
        return right  # or left, they are the same


# @lc code=end
