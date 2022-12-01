class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        d = len(s) // 2
        return sum(ch.lower() in "aeiou" for ch in s[:d]) == sum(ch.lower() in "aeiou" for ch in s[d:])
