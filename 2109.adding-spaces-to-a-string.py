from typing import List


# @leet start
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        word_start = 0
        result = []

        for space in spaces:
            result.append(s[word_start:space])
            word_start = space
            result.append(" ")

        result.append(s[word_start:])

        return "".join(result)


# @leet end

