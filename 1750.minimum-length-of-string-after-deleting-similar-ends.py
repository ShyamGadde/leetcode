#
# @lc app=leetcode id=1750 lang=python3
#
# [1750] Minimum Length of String After Deleting Similar Ends
#
# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/
#
# algorithms
# Medium (44.91%)
# Likes:    944
# Dislikes: 77
# Total Accepted:    103.4K
# Total Submissions: 190.1K
# Testcase Example:  '"ca"'
#
# Given a string s consisting only of characters 'a', 'b', and 'c'. You are
# asked to apply the following algorithm on the string any number of
# times:
#
#
# Pick a non-empty prefix from the string s where all the characters in the
# prefix are equal.
# Pick a non-empty suffix from the string s where all the characters in this
# suffix are equal.
# The prefix and the suffix should not intersect at any index.
# The characters from the prefix and suffix must be the same.
# Delete both the prefix and the suffix.
#
#
# Return the minimum length of s after performing the above operation any
# number of times (possibly zero times).
#
#
# Example 1:
#
#
# Input: s = "ca"
# Output: 2
# Explanation: You can't remove any characters, so the string stays as is.
#
#
# Example 2:
#
#
# Input: s = "cabaabac"
# Output: 0
# Explanation: An optimal sequence of operations is:
# - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
# - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
# - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
# - Take prefix = "a" and suffix = "a" and remove them, s = "".
#
# Example 3:
#
#
# Input: s = "aabccabba"
# Output: 3
# Explanation: An optimal sequence of operations is:
# - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
# - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s only consists of characters 'a', 'b', and 'c'.
#
#
#


# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1

        while left < right and s[left] == s[right]:
            tmp = s[left]

            # By also checking for equality, we ensure that we are correctly handling the case where all remaining characters are the same, e.g,. 'aa'.
            # If we only checked for 'left < right' or 'right > left', the loops would stop one step early in such a scenario.
            while left <= right and s[left] == tmp:
                left += 1

            while right >= left and s[right] == tmp:
                right -= 1

        return (right - left) + 1


# @lc code=end
