#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = {"+", "-", "*", "/"}
        stack = []
        operator_func = {
            "+": lambda y, x: x + y,
            "-": lambda y, x: x - y,
            "*": lambda y, x: x * y,
            "/": lambda y, x: int(x / y),
        }

        for token in tokens:
            if token in operators:
                stack.append(operator_func[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))

        return stack.pop()


# @lc code=end
