from typing import List
from collections import Counter


# @leet start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = Counter(nums1) & Counter(nums2)

        return [num for num, count in intersection.items() for _ in range(count)]


# @leet end
