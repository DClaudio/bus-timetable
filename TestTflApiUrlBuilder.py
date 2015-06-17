import unittest
from TflApiUrlBuilder import *

class TestTflApiUrlBuilder(unittest.TestCase):

	def test_url_builder(self):
		action_category = 'StopPoint'
		action = 'Arrivals'
		station_id = '490012375E'
		expected_url = 'https://api.tfl.gov.uk/StopPoint/Arrivals?ids=490012375E&app_id=7df32329&app_key=b13d2099c8c5b37c0cbbe29c7b37faae'

		url_builder = TflApiUrlBuilder(action_category)
		url = url_builder.with_action(action).with_station_id(station_id).build_url()
		self.assertEqual(url, expected_url)


unittest.main()