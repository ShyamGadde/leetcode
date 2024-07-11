# @leet start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack: list[str] = []

        for c in s:
            if c == ")":
                tmp: list[str] = []
                while stack[-1] != "(":
                    tmp.append(stack.pop())
                stack.pop()
                stack += tmp
            else:
                stack.append(c)

        return "".join(stack)


# @leet end
