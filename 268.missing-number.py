#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#


# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_number = len(nums)
        for i, num in enumerate(nums):
            missing_number ^= i ^ num
        return missing_number


# @lc code=end
