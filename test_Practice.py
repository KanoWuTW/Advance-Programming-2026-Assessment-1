import unittest
from practical import Ticket, StudentTicket, Booking


class TestGetPrice(unittest.TestCase):
    def test_1(self):
        # setup
        t1 = Ticket("film1", 5)
        # Act
        result = t1.get_price()
        # Assert
        self.assertEqual(result, 5)

    def test_student(self):
        # setup
        s1 = StudentTicket("film1", 5, 0.85)
        # Act
        result = s1.get_price()
        # Assert
        self.assertEqual(result, 4.25)

    def test_booking(self):
        # setup
        book = Booking()
        book.add_ticket(StudentTicket("film1", 5, 0.85))
        book.add_ticket(Ticket("film1", 5))
        # Act
        cost = book.total_cost()
        num = book.ticket_count()
        # Assert
        self.assertEqual(cost, 9.25)
        self.assertEqual(num, 2)


if __name__ == "__main__":
    unittest.main()
