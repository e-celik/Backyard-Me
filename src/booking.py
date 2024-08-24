class Booking:
    def __init__(self, duration, boundShow, boundBand=None):
        self.duration = duration
        self.boundShow = boundShow
        self.boundBand = boundBand

    def alertBookingOfBooking(self, band):
        print(f"Booking.py says: Booking has been booked by {band.name}!")