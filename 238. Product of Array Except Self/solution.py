#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        out = [1] * length

        prefix = 1
        for i in range(length):
            out[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(length):
            out[~i] *= postfix
            postfix *= nums[~i]

        return out


# @lc code=end


# Time complexity: O(n)
# Space complexity: O(1) (we are ignoring the output; the computation takes O(1))
