#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
import collections
import itertools


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        blocks = collections.defaultdict(set)

        for row, col in itertools.product(range(9), range(9)):
            num = board[row][col]
            block = (row // 3) * 3 + col // 3
            if num != "." and (
                num in rows[row] or num in cols[col] or num in blocks[block]
            ):
                return False
            rows[row].add(num)
            cols[col].add(num)
            blocks[block].add(num)
        return True


# @lc code=end
