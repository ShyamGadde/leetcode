class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([ch for ch in s.lower() if ch.isalnum()])
        return s == s[::-1]

# Time complexity: O(N)
# Space complexity: O(N)
