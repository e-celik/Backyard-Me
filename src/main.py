from datetime import datetime, timedelta
from booking import Booking
from band import Band

def main(): # tests for now
    myOldBooking = Booking((datetime.now(), datetime.now()+timedelta(seconds=30)), "Sixty-Third")
    myNewBooking = Booking((datetime.now()+timedelta(seconds=-60), datetime.now()+timedelta(seconds=-30)), "UCSD")
    myBand = Band("Poserz", "Pozers@me.com", [myOldBooking])
    myBand.bookBooking(myNewBooking)

if __name__ == '__main__':
    main()