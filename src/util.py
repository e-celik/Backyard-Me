from datetime import datetime
from booking import Booking
from typing import List

# returns boolean of whether or not the given time slot can fit into the given schedule i.e., no overlap
def fitsInSchedule(span, schedule: List[Booking]):
    start_time, end_time = span
    for obligation in schedule:
        obligation_start, obligation_end = obligation.duration
        if (start_time < obligation_end) and (end_time > obligation_start):
            return False  # The band has an overlap in the schedule
    # No overlap, return true
    return True
            
