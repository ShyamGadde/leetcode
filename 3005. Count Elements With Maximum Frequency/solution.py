from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_ = max(freq.values())

        return sum(freq[x] == max_ for x in nums)
