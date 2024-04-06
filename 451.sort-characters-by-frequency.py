#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

from collections import Counter


# @lc code=start
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join(char * freq for char, freq in Counter(s).most_common())


# @lc code=end
