class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pair = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for ch in s:
            if not bracket_pair.get(ch):
                stack.append(ch)
                continue
            if not stack or stack[-1] != bracket_pair[ch]:
                return False
            stack.pop()
        return not stack


# Time complexity: O(n)
# Space complexity: O(n)
