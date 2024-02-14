#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = filter(lambda x: x > 0, nums)
        negative = filter(lambda x: x < 0, nums)

        res = []
        for pair in zip(positive, negative):
            res.extend(pair)

        return res


# @lc code=end
