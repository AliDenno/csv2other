import unittest
import bin
from bin.validate_record import validate_rating, validate_name, validate_url

class TestRecordValidation(unittest.TestCase):
    def test_rating_validation(self):
        self.assertEqual(validate_rating(1),1)
        self.assertEqual(validate_rating(0),1)
        self.assertEqual(validate_rating(6),0)
        self.assertEqual(validate_rating(-10),0)
        self.assertEqual(validate_rating(""),0)
        self.assertEqual(validate_rating(" "),0)
        self.assertEqual(validate_rating("String"),0)
        self.assertEqual(validate_rating(1000000),0)
        self.assertEqual(validate_rating(3),1)
        self.assertEqual(validate_rating(-100000),0)

    def test_name_validation(self):
        self.assertEqual(validate_name(""),0)
        self.assertEqual(validate_name(" "),0)
        self.assertEqual(validate_name("Hotel Name"),1)
        self.assertEqual(validate_name(100),0)
        self.assertEqual(validate_name(-4400),0)

    def test_url_validation(self):
        self.assertEqual(validate_url(""),0)
        self.assertEqual(validate_url(" "),0)
        self.assertEqual(validate_url(100),0)
        self.assertEqual(validate_url(-4400),0)
        self.assertEqual(validate_url("Nice URL"),0)
        self.assertEqual(validate_url("https://www.google.de"),1)
        
if __name__ == '__main__':
    unittest.main()

 