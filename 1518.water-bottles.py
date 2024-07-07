# @leet start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles

        while numBottles >= numExchange:
            full_water_bottles, empty_bottles = divmod(numBottles, numExchange)
            total += full_water_bottles
            numBottles = full_water_bottles + empty_bottles

        return total


# @leet end
