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
