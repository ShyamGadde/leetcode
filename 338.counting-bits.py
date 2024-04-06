#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#


# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
            # i >> 1 essentially divides i by 2 and rounds down
            # 8 has same number of 1s as 4
            # 9 has same number of 1s as 4 + 1
            # i & 1 is 1 if i is odd, 0 if i is even
        return res


# @lc code=end
