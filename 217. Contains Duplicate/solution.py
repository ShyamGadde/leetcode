from typing import *

#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True


# Time complexity: O(NLogN)
# Space complexity: O(1)

# @lc code=end

# Alternate solution
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashset = set()
#         for num in nums:
#             if num in hashset:
#                 return True
#             hashset.add(num)

# Time complexity: O(N)
# Space complexity: O(N)
