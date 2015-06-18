import unittest
import json
from TflArrivalsResponseParser import *
from TflApiUrlBuilder import *

class TestTflArrivalsResponseParser(unittest.TestCase):

	def test_parse_response(self):
		eample_response_file = open('resources/example_response.json')
		response_string = eample_response_file.read()
		eample_response_file.close()
		expected_result_file = open('resources/expected_result.json')
		expected_result = json.loads(expected_result_file.read())
		expected_result_file.close()

		responseParser = TflArrivalsResponseParser()		
		self.assertEqual(responseParser.get_formated_response(response_string), expected_result)

class TestTflApiUrlBuilder(unittest.TestCase):

	def test_url_builder(self):
		action_category = 'StopPoint'
		action = '%7Bids%7D/Arrivals'
		station_id = '490012375E'
		expected_url = 'https://api.tfl.gov.uk/StopPoint/%7Bids%7D/Arrivals?ids=490012375E' \
						+'&app_id=7df32329&app_key=b13d2099c8c5b37c0cbbe29c7b37faae'

		url_builder = TflApiUrlBuilder(action_category)
		url = url_builder.with_action(action).with_station_id(station_id).build_url()
		self.assertEqual(url, expected_url)



unittest.main()