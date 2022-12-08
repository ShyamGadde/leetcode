from typing import *

#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
# @lc code=end

# Alternate solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in hashmap:
            if num in hashmap:
                return True
            hashmap[num] = 1
        return False

"""
Why not use dictionary?
>>> We can use a dictionary if we want to, but there is no need to, as don't have to keep a track of the count of the elements rather just check if we have already encountered the element before. Dictionary would be ideal if we were checking for something like, "an element that appears at least thrice, as we can't tell if the element have already appeared twice or thrice using a set. As far as time and space complexity are concerned, I'm sure not sure if one is better than the other."
"""
