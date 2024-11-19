from typing import List
from collections import defaultdict


# @leet start
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum, current_sum, start = 0, 0, 0
        freq = defaultdict(int)

        for i in range(k):
            current_sum += nums[i]
            freq[nums[i]] += 1

        if len(freq) == k:
            max_sum = current_sum

        for end in range(k, len(nums)):
            current_sum -= nums[start]
            freq[nums[start]] -= 1

            current_sum += nums[end]
            freq[nums[end]] += 1

            if freq[nums[start]] == 0:
                del freq[nums[start]]

            start += 1

            if len(freq) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum


# @leet end

