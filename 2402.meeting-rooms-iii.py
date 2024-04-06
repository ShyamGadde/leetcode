#
# @lc app=leetcode id=2402 lang=python3
#
# [2402] Meeting Rooms III
#
import heapq
from typing import List


# @lc code=start
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = list(range(n))
        used: list[tuple[int, int]] = []  # (end, room)
        meetings_per_room = [0] * n  # Meetings scheduled for each room

        for start, end in meetings:
            while used and used[0][0] <= start:  # Remove ended meetings
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            if not available:
                end_, room = heapq.heappop(used)
                # Update end time to prev meeting end time + current meeting duration
                end = end_ + (end - start)
                heapq.heappush(available, room)

            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            meetings_per_room[room] += 1

        return meetings_per_room.index(max(meetings_per_room))


# @lc code=end

if __name__ == "__main__":
    n = 2
    meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
    print(Solution().mostBooked(n, meetings))
