class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0

        for sell in range(1, len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            max_profit = max(prices[sell] - prices[buy], max_profit)
        return max_profit

# Time complexity: O(N)
# Space complexity: O(1)
