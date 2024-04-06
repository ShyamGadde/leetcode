# @before-stub-for-debug-begin
from python3problem1 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_elems = {}

        for i, n in enumerate(nums):
            if (diff := target - n) in prev_elems:
                return [prev_elems[diff], i]
            prev_elems[n] = i

# @lc code=end
