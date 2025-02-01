from typing import List


# @leet start
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev_parity = nums[0] & 1

        for i in range(1, len(nums)):
            parity = nums[i] & 1
            if parity == prev_parity:
                return False
            prev_parity = parity

        return True


# @leet end

