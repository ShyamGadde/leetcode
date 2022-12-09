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

# Time complexity: O(N)
# Space complexity: O(1)

# @lc code=end

# Alternate solution
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashmap = {}
#         for num in hashmap:
#             if num in hashmap:
#                 return True
#             hashmap[num] = 1
#         return False

# Time complexity: O(N)
# Space complexity: O(N)


# Alternate solution #2
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashset = set()
#         for num in nums:
#             if num in hashset:
#                 return True
#             hashset.add(num)

# Time complexity: O(N)
# Space complexity: O(N)

"""
Why not use dictionary?
>>> We can use a dictionary if we want to, but there is no need to, as don't have to keep a track of the count of the elements rather just check if we have already encountered the element before. Dictionary would be ideal if we were checking for something like, "an element that appears at least thrice, as we can't tell if the element have already appeared twice or thrice using a set. As far as time and space complexity are concerned, I'm sure not sure if one is better than the other (maybe dictionary uses more space as it stores keys and values)."
"""
