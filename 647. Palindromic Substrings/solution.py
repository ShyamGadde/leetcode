#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0

        for i in range(len(s)):
            # Odd length palindromes
            count += self.countPalindromes(s, i, i)
            # Even length palindromes
            count += self.countPalindromes(s, i, i + 1)

        return count

    def countPalindromes(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count


# @lc code=end
