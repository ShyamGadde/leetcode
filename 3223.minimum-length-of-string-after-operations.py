from collections import Counter


# @leet start
class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)

        delete_count = 0

        for f in freq.values():
            if f % 2 == 1:
                # If frequency is odd, delete all except one
                delete_count += f - 1
            else:
                # If frequency is even, delete all except two
                delete_count += f - 2

        return len(s) - delete_count


# @leet end

