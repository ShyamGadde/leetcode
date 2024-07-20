from typing import List
import heapq


# @leet start
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
                ladders -= 1
                bricks -= heapq.heappop(heap)

        return len(heights) - 1


# @leet end
