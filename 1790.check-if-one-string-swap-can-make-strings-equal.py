from collections import Counter


# @leet start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        mismatches = sum(s1[i] != s2[i] for i in range(len(s1)))

        # If mismatches are more than 2, then one character swap can't make the strings equal.
        if mismatches > 2:
            return False
        else:
            return Counter(s1) == Counter(s2)


# @leet end

