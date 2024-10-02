class MyCalendarTwo:
    def __init__(self):
        # Initialize two lists to keep track of single and double bookings
        self.single_bookings = []
        self.double_bookings = []

    def book(self, start: int, end: int) -> bool:
        # Check if this booking overlaps with any double booking
        for double_start, double_end in self.double_bookings:
            # If there is any overlap with double bookings, return False (triple booking)
            if max(start, double_start) < min(end, double_end):
                return False

        # If no triple booking, check overlap with single bookings to add to double bookings
        for single_start, single_end in self.single_bookings:
            # If there is overlap with a single booking, we create a double booking for the overlapping part
            if max(start, single_start) < min(end, single_end):
                overlap_start = max(start, single_start)
                overlap_end = min(end, single_end)
                self.double_bookings.append((overlap_start, overlap_end))

        # Add the new booking to the single bookings
        self.single_bookings.append((start, end))

        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
