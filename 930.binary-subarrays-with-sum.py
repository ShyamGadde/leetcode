#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#
# https://leetcode.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (55.81%)
# Likes:    3426
# Dislikes: 110
# Total Accepted:    179.1K
# Total Submissions: 295.5K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# Given a binary array nums and an integer goal, return the number of non-empty
# subarrays with a sum goal.
#
# A subarray is a contiguous part of the array.
#
#
# Example 1:
#
#
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#
#
# Example 2:
#
#
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# nums[i] is either 0 or 1.
# 0 <= goal <= nums.length
#
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x):
            """Return the number of subarrays with sum <= x."""
            if x < 0:
                return 0

            res = 0
            left = 0
            cur_sum = 0

            for right in range(len(nums)):
                cur_sum += nums[right]
                while cur_sum > x:
                    cur_sum -= nums[left]
                    left += 1
                # Number of subarrays ending at right and having sum <= x
                res += right - left + 1
            return res

        return helper(goal) - helper(goal - 1)


# @lc code=end
