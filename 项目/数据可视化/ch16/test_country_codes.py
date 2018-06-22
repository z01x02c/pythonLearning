import unittest
from country_codes import get_country_code

class NamesTestCase(unittest.TestCase):
    def test_country_code(self):
        code = get_country_code('China')
        self.assertEqual(code,'cn')

unittest.main()

    

