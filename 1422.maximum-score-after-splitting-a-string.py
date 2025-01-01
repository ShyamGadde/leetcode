# @leet start
class Solution:
    def maxScore(self, s: str) -> int:
        right = s.count("1")
        left = 0
        max_score = 0

        for i in range(len(s) - 1):
            if s[i] == "1":
                right -= 1
            else:
                left += 1

            max_score = max(max_score, left + right)

        return max_score


# @leet end

