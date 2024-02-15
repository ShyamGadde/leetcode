#
# @lc app=leetcode id=2971 lang=python3
#
# [2971] Find Polygon With the Largest Perimeter
#

# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res = -1
        total = sum(nums)

        for x in nums:
            total -= x
            if x < total:
                res = x + total
                break

        return res


# @lc code=end
