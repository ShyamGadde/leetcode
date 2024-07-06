# @leet start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # In n - 1 seconds the pillow completes a full round
        full_rounds, remaining_time = divmod(time, n - 1)

        if full_rounds % 2 == 0:
            return remaining_time + 1  # 0-based index to 1-based index
        else:
            return n - remaining_time


# @leet end
