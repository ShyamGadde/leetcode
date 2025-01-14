from typing import List
from collections import defaultdict


# @leet start
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        count = defaultdict(int)
        common_count = 0

        for i in range(len(A)):
            count[A[i]] += 1
            count[B[i]] += 1

            # If count of `A[i]` is 2, it means `A[i]` is common in `A` and `B`.
            if count[A[i]] == 2:
                common_count += 1

            # If `A[i]` is not equal to `B[i]` and count of `B[i]` is 2,
            # it means `B[i]` is common in `A` and `B`.
            if A[i] != B[i] and count[B[i]] == 2:
                common_count += 1

            res.append(common_count)

        return res


# @leet end

