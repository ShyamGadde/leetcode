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
        self.operators = ["+", "-", "*", "/"]
        self.stack = []

        for token in tokens:
            if token in self.operators:
                self.evaluate(token)
            else:
                self.stack.append(int(token))

        return self.stack.pop()

    def evaluate(self, operator):
        num2 = self.stack.pop()
        num1 = self.stack.pop()
        if operator == "+":
            self.stack.append(num1 + num2)
        elif operator == "-":
            self.stack.append(num1 - num2)
        elif operator == "*":
            self.stack.append(num1 * num2)
        elif operator == "/":
            self.stack.append(int(num1 / num2))
        else:
            raise ValueError("Invalid operator")


# @lc code=end
