import unittest
import assessment1

class TestAssessment1(unittest.TestCase):
    def setup(self):
        pass
    def testmain(self):
        flight = assessment1.main()
        seating_areas = flight.seating_areas
        total_areas = len(seating_areas)
        self.assertEquals(total_areas,3)
        seating_area = seating_areas['Firstclass']
        self.assertEquals(seating_area.booking_class.type,'Firstclass')
        self.assertEquals(seating_area.seat_count,5)
        self.assertEquals(len(seating_area.seats_remaining),5)
        seating_area = seating_areas['Business']
        self.assertEquals(seating_area.booking_class.type,'Business')
        self.assertEquals(seating_area.seat_count,10)
        self.assertEquals(len(seating_area.seats_remaining),10)
        seating_area = seating_areas['Economy']
        self.assertEquals(seating_area.booking_class.type,'Economy')
        self.assertEquals(seating_area.seat_count,15)
        self.assertEquals(len(seating_area.seats_remaining),15)
        #economy = BookingClass("Economy") 
        #firstClass_seats = SeatingArea(economy, start_row=1, row_count=5, seats_per_row=3)


if __name__ == '__main__':
    unittest.main()
    #for booking_class, seating_area in flight.seating_areas.items():
        #self.assertEquals()
