#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#


# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # for i in range(len(digits)):
        #     if digits[~i] < 9:
        #         digits[~i] += 1
        #         return digits
        #     digits[~i] = 0
        # return [1] + [0] * len(digits)

        return map(int, str(int("".join(map(str, digits))) + 1))


# @lc code=end
