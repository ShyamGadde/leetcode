#
# @lc app=leetcode id=2962 lang=python3
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
#
# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/
#
# algorithms
# Medium (44.72%)
# Likes:    360
# Dislikes: 18
# Total Accepted:    27.7K
# Total Submissions: 54.5K
# Testcase Example:  '[1,3,2,3,3]\n2'
#
# You are given an integer array nums and a positive integer k.
#
# Return the number of subarrays where the maximum element of nums appears at
# least k times in that subarray.
#
# A subarray is a contiguous sequence of elements within an array.
#
#
# Example 1:
#
#
# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are:
# [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
#
#
# Example 2:
#
#
# Input: nums = [1,4,2,1], k = 3
# Output: 0
# Explanation: No subarray contains the element 4 at least 3 times.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^6
# 1 <= k <= 10^5
#
#
#
from typing import List


# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        start = count = ans = 0

        for num in nums:
            if num == max_num:
                count += 1

            while count > k or (count == k and nums[start] != max_num):
                if nums[start] == max_num:
                    count -= 1
                start += 1

            if count == k:
                # `start` is the first index of the subarray
                # All subarrays starting at `0` to `start` will have
                # max_num at least k times
                # So, we can add start + 1 to the answer,
                # as the index is 0-based
                ans += start + 1

        return ans


# @lc code=end
