#
# @lc app=leetcode id=1481 lang=python3
#
# [1481] Least Number of Unique Integers after K Removals
#
from collections import Counter


# @lc code=start
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        res = len(freq)  # Number of unique integers

        freq_freq = [0] * (len(arr) + 1)  # Number of elements with frequency i
        for f in freq.values():
            freq_freq[f] += 1

        for i in range(1, len(freq_freq)):
            removals = freq_freq[i] * i
            if removals <= k:
                res -= freq_freq[i]
                k -= removals
            else:
                res -= k // i
                # Eg. Let's say k = 15, i = 6 and freq_freq[i] = 3,
                # i.e., there are 3 elements with frequency 6. Then removals = 6 * 3 = 18.
                # Hence, we can only eliminate 2 unique integers from they array.
                break

        return res


# @lc code=end
