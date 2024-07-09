from typing import List


# @leet start
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        net_waiting_time = 0
        next_idle_time = 0

        for customer in customers:
            if next_idle_time < customer[0]:
                next_idle_time = customer[0] + customer[1]
                net_waiting_time += customer[1]
            else:
                next_idle_time += customer[1]
                net_waiting_time += next_idle_time - customer[0]

        return net_waiting_time / len(customers)


# @leet end
