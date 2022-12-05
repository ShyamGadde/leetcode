class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([ch for ch in s.lower() if ch.isalnum()])
        return s == s[::-1]

# Time complexity: O(N)
# Space complexity: O(N) (Technically the same variable 's' is used so many be not but maybe for s[::-1])


# Alternative solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()

        while l < r:
            while l < r and not self.alnum(s[l]):
                l += 1
            while r > l and not self.alnum(s[r]):
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def alnum(self, c):
        return (65 <= ord(c) <= 90 or
                97 <= ord(c) <= 122 or
                48 <= ord(c) <= 57)

# Time complexity; O(N)
# Space complexity: O(1)
