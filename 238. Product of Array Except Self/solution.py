#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        res = [1] * length

        prefix_prod = 1
        for i in range(length):
            res[i] = prefix_prod
            prefix_prod *= nums[i]

        postfix_prod = 1
        for i in range(length):
            res[~i] *= postfix_prod
            postfix_prod *= nums[~i]

        return res


# @lc code=end


# Time complexity: O(n)
# Space complexity: O(1) (we are ignoring the output; the computation takes O(1))
