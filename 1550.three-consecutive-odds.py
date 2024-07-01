from typing import List


# @leet start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0

        for x in arr:
            if x & 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0

        return False


# @leet end
