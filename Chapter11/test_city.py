import city_functions
import unittest

class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        ans = city_functions.city_country("vancouver", "canada")
        self.assertEqual(ans, 'Vancouver, Canada')

    def test_populations(self):
        ans = city_functions.population("vancouver", "canada", "150")
        self.assertEqual(ans, "Vancouver, Canada, 150")

if __name__ == '__main__':
    unittest.main()