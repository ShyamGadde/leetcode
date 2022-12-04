class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pair = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for ch in s:
            if ch not in bracket_pair:
                stack.append(ch)
                continue
            if not stack or stack[-1] != bracket_pair[ch]:
                return False
            stack.pop()
        return not stack


# Time complexity: O(N)
# Space complexity: O(N)
