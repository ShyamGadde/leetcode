from typing import List


# @leet start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = [0] * len(code)

        if k == 0:
            return res

        # For the first element, we need to calculate the sum of the next/prev k elements
        if k > 0:
            res[0] = sum(code[1 : k + 1])
        else:
            res[0] = sum(code[k:])

        for i in range(1, len(code)):
            if k > 0:
                res[i] = (res[i - 1] - code[i]) + code[(i + k) % len(code)]
            else:
                res[i] = (res[i - 1] - code[(i + k - 1)]) + code[i - 1]

        return res


# @leet end

