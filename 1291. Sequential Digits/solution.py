#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#

from collections import deque


# @lc code=start
class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        res = []
        queue = deque(range(1, 10))

        while queue:
            num = queue.popleft()
            if low <= num <= high:
                res.append(num)
            if (last_digit := num % 10) < 9:
                queue.append(num * 10 + last_digit + 1)

        return res


# @lc code=end
