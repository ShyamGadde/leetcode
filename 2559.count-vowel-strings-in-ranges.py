from typing import List


# @leet start
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")

        def is_vowel_string(word: str) -> bool:
            return word[0] in vowels and word[-1] in vowels

        # Compute prefix sums for words that satisfy the condition
        prefix_sum = [0] * (len(words) + 1)
        for i in range(len(words)):
            prefix_sum[i + 1] = prefix_sum[i] + is_vowel_string(words[i])

        ans = []
        for left, right in queries:
            # We use prefix_sum to get the count of vowel strings in the range [left, right].
            # prefix_sum[right + 1] gives the count of vowel strings from the start to the (right + 1)-th word.
            # prefix_sum[left] gives the count of vowel strings from the start to the left-th word.
            # By subtracting prefix_sum[left] from prefix_sum[right + 1], we get the count of vowel strings
            # in the range [left, right].
            # The reason we use right + 1 is because prefix_sum includes an extra initial 0 at index 0,
            # which shifts the indices by 1. This way, prefix_sum[right + 1] correctly represents the count
            # up to the right-th word.
            # This approach ensures that we include both the left and right indices in our range.
            # Additionally, when left is 0, prefix_sum[left] is 0, so subtracting it does not affect the result.
            ans.append(prefix_sum[right + 1] - prefix_sum[left])

        return ans


# @leet end

