from typing import List


# @leet start
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # Will work as long as the age is not above 100
        return sum(detail[11:13] > "60" for detail in details)


# @leet end

