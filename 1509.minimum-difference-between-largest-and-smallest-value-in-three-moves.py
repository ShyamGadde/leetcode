from typing import List


# @leet start
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        result = float("inf")

        for i in range(4):
            result = min(result, nums[-4 + i] - nums[i])

        return result


# @leet end
