#
# @lc app=leetcode id=1642 lang=python3
#
# [1642] Furthest Building You Can Reach
#
import heapq


# @lc code=start
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []  # Max heap

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue

            heapq.heappush(heap, -diff)
            bricks -= diff

            if bricks < 0:
                if ladders == 0:
                    return i
                # If we don't have enough bricks, use a ladder instead of bricks
                # on the largest difference in height so far.
                ladders -= 1
                bricks -= heapq.heappop(heap)

        return len(heights) - 1


# @lc code=end
