import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print("WELCOME TO AIR LINES BOOKING:")
print ("PLEASE KEEP SOCIAL DISTANCE AND WEAR MASK")
print("Booking for Bangalore to Chennai")


class BookingClass:
    ECONOMY = 'Economy'
    BUSINESS = 'Business'
    FIRSTCLASS = 'Firstclass'
    def __init__ (self,type:str,price:int):
        self.type = type
        self.price = price

class Seat:
    def __init__(self, row_number: int, letter: str, booking_class:BookingClass):
        self.row_number = row_number
        self.letter = letter
        self.booking_class = booking_class

    def __str__(self):
        return '{}-{}{}'.format(self.booking_class.type, self.row_number, self.letter)


class SeatingArea:
    def __init__(self, booking_class:BookingClass, start_row: int, row_count: int, seats_per_row: int):
        self.booking_class = booking_class
        self.seat_count = row_count * seats_per_row
        self.seats_remaining = []

        for row_number in range(start_row, row_count + start_row):
            for seat_number in range(seats_per_row):
                new_seat = Seat(row_number, letters[seat_number], booking_class)
                self.seats_remaining.append(new_seat)


class Flight:
    def __init__(self, economy_seats: SeatingArea, business_seats: SeatingArea, firstClass_seats: SeatingArea):
        
        self.seating_areas = {
            BookingClass.ECONOMY: economy_seats,
            BookingClass.BUSINESS: business_seats,
            BookingClass.FIRSTCLASS: firstClass_seats
        }

    def print_statistics(self):
        for booking_class, seating_area in self.seating_areas.items():
            print('{}: {}% available, Price: Rs.{}'.format(
                booking_class,
                len(seating_area.seats_remaining) / seating_area.seat_count * 100,
                seating_area.booking_class.price))

    def remaining_seat_count(self, booking_class: str):
        return len(self.seating_areas[booking_class].seats_remaining)

    def get_seat(self, booking_class: str):
        return self.seating_areas[booking_class].seats_remaining.pop()


class Passenger:
    def __init__(self, name: str):
        self.name = name
        self.booking_id = None
        self.seat = None

    def has_booked(self):
        return self.booking_id is not None

    def book(self, flight: Flight, booking_class: str):
        if flight.remaining_seat_count(booking_class) != 0:
            self.seat = flight.get_seat(booking_class)
            self.booking_id = random.Random().randrange(1000, 5000)
            return True
        return False

    def __str__(self):
        return 'Name:{}\nBooking Id:{}\nSeat:{}'.format(self.name, self.booking_id, self.seat)

def main():
    firstClass = BookingClass(BookingClass.FIRSTCLASS,5000)
    business = BookingClass(BookingClass.BUSINESS,3000)
    economy = BookingClass(BookingClass.ECONOMY,1000)

    firstClass_seats = SeatingArea(firstClass, start_row=1, row_count=5, seats_per_row=1)
    business_seats = SeatingArea(business, start_row=6, row_count=5, seats_per_row=2)
    economy_seats= SeatingArea(economy, start_row=11, row_count=5, seats_per_row=3)
    flight = Flight(economy_seats, business_seats, firstClass_seats)
    return flight

def getInput(flight : Flight):
    classType = None
    name = str(input('Enter the Passenger Name:'))
    option = str(input('Select the Class: \n 1. First Class\n 2. Business Class\n 3. Economy Class\n Please select the option:'))
    otherTypes = []
    if option == "1":
        classType = BookingClass.FIRSTCLASS
        otherTypes.append(BookingClass.BUSINESS)
        otherTypes.append(BookingClass.ECONOMY)
    
    elif option == "2":
        classType = BookingClass.BUSINESS
        otherTypes.append(BookingClass.FIRSTCLASS)
        otherTypes.append(BookingClass.ECONOMY)
    elif option == "3":
        classType = BookingClass.ECONOMY
        otherTypes.append(BookingClass.BUSINESS)
        otherTypes.append(BookingClass.FIRSTCLASS)
    #else:
        #print("seat is not available pls booking on another flight")
    bookRslt = False
    cnt = 0
    passenger = Passenger(name)
    while not bookRslt:
        bookRslt = passenger.book(flight, classType)
        if bookRslt:
            print('\n{}'.format(passenger))
            break
        else:
            print('No seats available in {} trying to book in {} '.format(classType, otherTypes[cnt]))
            classType = otherTypes[cnt]
            cnt += 1
            if cnt == 2:
                print('No seats available in any class. Please try in another flight.')
                break
    print('\nFlight Statistics:\n')
    flight.print_statistics()
    return bookRslt

    
if __name__ == '__main__':
    flight = main()
    while True:
      bookRslt = getInput(flight)
      if not bookRslt:
          break