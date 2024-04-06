class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()

        while left < right:
            while left < right and not self.alnum(s[left]):
                left += 1
            while right > left and not self.alnum(s[right]):
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def alnum(self, c):
        return 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122 or 48 <= ord(c) <= 57


# Time complexity; O(N)
# Space complexity: O(1)
