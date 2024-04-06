# @before-stub-for-debug-begin
# from python3problem190 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#


# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans = (ans << 1) | (n & 1)
            n >>= 1
        return ans


# @lc code=end

# Complexity Analysis
# Time complexity: O(1). Though we have a loop in the algorithm, the
# number of iteration is fixed regardless the input, since the
# integer is of fixed-size (32-bits) in our problem.
# Space complexity: O(1), since the consumption of memory is constant
# regardless the input.
