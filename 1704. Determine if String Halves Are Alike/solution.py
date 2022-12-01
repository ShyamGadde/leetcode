class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        from collections import Counter

        s = s.casefold()
        d = len(s) // 2

        a_vowel_count = sum(v for k, v in Counter(s[:d]).items() if k in ('a', 'e', 'i', 'o', 'u'))
        b_vowel_count = sum(v for k, v in Counter(s[d:]).items() if k in ('a', 'e', 'i', 'o', 'u'))

        return a_vowel_count == b_vowel_count
