from typing import List
from collections import Counter


# @leet start
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        nums.sort(key=lambda x: (freq[x], -x))

        return nums


# @leet end

