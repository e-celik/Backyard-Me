from datetime import datetime
from booking import Booking
from util import fitsInSchedule
from typing import List

class Band:
    def __init__(self, name, contact, schedule: List[Booking]):
        self.name = name  # str
        self.contact = contact  # list of strs
        self.schedule = schedule  # array of non-overlapping bookings
        # other properties idk yet

    # attempt to book a booking, a.k.a., attempt to claim a performing spot at a show
    # should work if the band has no other obligations at that time.
    def bookBooking(self, booking: Booking):

        if fitsInSchedule(booking.duration, self.schedule):
            self.schedule.append(booking)
            booking.alertBookingOfBooking(self)
            self.alertBandOfBooking(booking)
            return True
        else:
            return False
        
    def alertBandOfBooking(self, booking):
        # TODO: Lots, like actually email or text.
        print(f"Band.py says: Booked show at {list(map(lambda time: time.strftime("%X"), booking.duration))}, email the band or something at {self.contact}.\n")


