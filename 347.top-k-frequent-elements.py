#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(list)

        for num, count in collections.Counter(nums).items():
            freq[count].append(num)

        result = []
        for count in range(max(freq.keys()), 0, -1):
            result.extend(freq[count])
            if len(result) >= k:
                return result[:k]

        return result[:k]


# @lc code=end
