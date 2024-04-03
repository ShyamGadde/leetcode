#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (41.18%)
# Likes:    15135
# Dislikes: 628
# Total Accepted:    1.5M
# Total Submissions: 3.7M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
#
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
#
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
#
#
#
# Constraints:
#
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
#
#
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
#
#
from typing import List


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path: set[tuple[int, int]] = set()

        def dfs(row, col, idx):
            if idx == len(word):
                return True

            if (
                row < 0
                or row >= ROWS
                or col < 0
                or col >= COLS
                or board[row][col] != word[idx]
                or (row, col) in path
            ):
                return False

            path.add((row, col))
            for r, c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if dfs(row + r, col + c, idx + 1):
                    return True
            path.remove((row, col))

            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False


# @lc code=end
