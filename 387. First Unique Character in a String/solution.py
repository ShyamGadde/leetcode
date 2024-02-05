#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

from collections import Counter


# @lc code=start
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)

        return next((i for i, c in enumerate(s) if freq[c] == 1), -1)


# @lc code=end
