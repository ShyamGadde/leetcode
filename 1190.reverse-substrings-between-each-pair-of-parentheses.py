# @leet start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        pair_idx = {}
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                j = stack.pop()
                pair_idx[i] = j
                pair_idx[j] = i

        res = []
        i, direction = 0, 1

        while i < len(s):
            if s[i] in "()":
                i = pair_idx[i]
                direction = -direction
            else:
                res.append(s[i])
            i += direction

        return "".join(res)


# @leet end
