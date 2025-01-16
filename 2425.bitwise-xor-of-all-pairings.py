from functools import reduce
from operator import xor
from typing import List


# @leet start
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0

        # If `nums2` length is odd, each element in `nums1` appears odd times in final result
        if len(nums2) & 1:
            result = reduce(xor, nums1)

        # If `nums1` length is odd, each element in `nums2` appears odd times in final result
        if len(nums1) & 1:
            result ^= reduce(xor, nums2)

        return result


# @leet end

