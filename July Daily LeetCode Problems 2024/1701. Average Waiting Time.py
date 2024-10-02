from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        total_waiting_time = 0

        for arrival, time_needed in customers:
            # Chef starts preparing the order when the customer arrives or when he's free, whichever is later
            start_time = max(current_time, arrival)
            # The time at which the order will be finished
            finish_time = start_time + time_needed
            # The waiting time for this customer
            waiting_time = finish_time - arrival
            # Accumulate the waiting time
            total_waiting_time += waiting_time
            # Update the current time to the finish time of the current order
            current_time = finish_time

        # Calculate the average waiting time
        average_waiting_time = total_waiting_time / len(customers)
        return average_waiting_time
