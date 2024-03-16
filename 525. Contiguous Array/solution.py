#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (46.91%)
# Likes:    7279
# Dislikes: 320
# Total Accepted:    363K
# Total Submissions: 765.5K
# Testcase Example:  '[0,1]'
#
# Given a binary array nums, return the maximum length of a contiguous subarray
# with an equal number of 0 and 1.
#
#
# Example 1:
#
#
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number
# of 0 and 1.
#
#
# Example 2:
#
#
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
#
#
#
from typing import List


# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cur_sum = max_len = 0
        # Stores the index of the first occurrence of a sum
        sum_idx = {0: -1}

        for i, x in enumerate(nums):
            cur_sum += 1 if x else -1
            # If the sum has been seen before, then the subarray between the two occurrences
            # has an equal number of 0s and 1s
            max_len = max(max_len, i - sum_idx.setdefault(cur_sum, i))

        return max_len


# @lc code=end
