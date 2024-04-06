#
# @lc app=leetcode id=2108 lang=python3
#
# [2108] Find First Palindromic String in the Array
#

# @lc code=start
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return next((word for word in words if word == word[::-1]), "")


# @lc code=end
