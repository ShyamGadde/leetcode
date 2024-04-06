#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#


# @lc code=start
class StockSpanner:
    def __init__(self) -> None:
        self.prices: list[int] = []
        self.stack: list[int] = []
        self.index = 0

    def next(self, price: int) -> int:
        self.prices.append(price)

        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()

        if not self.stack:
            self.stack.append(self.index)
            self.index += 1
            return self.index
        else:
            self.stack.append(self.index)
            self.index += 1
            return self.index - self.stack[-2] - 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end
