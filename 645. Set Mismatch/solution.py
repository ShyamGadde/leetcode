#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_s = len(nums) * (len(nums) + 1) // 2
        uniq_nums_sum = sum(set(nums))
        return [sum(nums) - uniq_nums_sum, sum_s - uniq_nums_sum]

# @lc code=end
