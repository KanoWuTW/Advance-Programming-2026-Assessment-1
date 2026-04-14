import unittest
from Assignment import StreamService


class TestRatingSys(unittest.TestCase):
    def test_shape_of_you(self):
        # setup
        ss = StreamService()
        # Act
        ss._StreamService__rating(ss.find_song_by_id(1))
        new_avg_rating, new_rating_num = ss.get_rating_test(1)

        # Assert
        self.assertEqual(new_avg_rating, 4.7)
        self.assertEqual(new_rating_num, 6)

    def test_Godzilla(self):
        # setup
        ss = StreamService()
        # Act
        ss._StreamService__rating(ss.find_song_by_id(23))
        new_avg_rating, new_rating_num = ss.get_rating_test(23)

        # Assert
        self.assertEqual(new_avg_rating, 3.7)
        self.assertEqual(new_rating_num, 7)


# if __name__ == "__main__":
#     unittest.main()
