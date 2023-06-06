#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = collections.defaultdict(list)
        max_count = 0
        for num, count in collections.Counter(nums).items():
            frequency[count].append(num)
            max_count = max(max_count, count)

        result = []
        for times in range(max_count, 0, -1):
            result.extend(frequency[times])
            if len(result) >= k:
                break

        return result if len(result) == k else result[:k]


# @lc code=end
