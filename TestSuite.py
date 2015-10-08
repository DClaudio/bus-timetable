import unittest
import json
from TflArrivalsResponseParser import *
from TflApiUrlBuilder import *

class TestTflArrivalsResponseParser(unittest.TestCase):

	def setUp(self):
		self.responseParser = TflArrivalsResponseParser() 

	@unittest.skip("not important")
	def test_format_seconds(self):
		seconds = 623 # equivalent to 10min 23sec
		expected_result = '10:23'	
		self.assertEqual(self.responseParser.format_seconds(seconds), expected_result)


	def test_parse_response(self):
		#load test data from resource files
		eample_response_file = open('resources/example_response.json')
		response_string = eample_response_file.read()
		eample_response_file.close()
		expected_result_file = open('resources/expected_result.json')
		expected_result = json.loads(expected_result_file.read())
		expected_result_file.close()

		# assert the results
		actual_result = self.responseParser.get_formated_response(response_string)
		self.assertEqual(actual_result, expected_result)

	def test_line_formatter(self):
		# bus number 
		expected_result_1 = ' 22 11:54 Piccad'
		expected_result_2 = '485  4:54 Wandsw'

		#build test data
		data_to_format1 = {
				'route': 22,
				'destination': 'Piccadilly Circus',
				'timeToStation': '11:54'
		}
		data_to_format2 = {
				'route': 485,
				'destination': 'Wandsworth',
				'timeToStation': '4:54'
		}

		actual_result_1 = self.responseParser.format_line(data_to_format1)
		actual_result_2 = self.responseParser.format_line(data_to_format2)

		self.assertEqual(actual_result_1,expected_result_1)
		self.assertEqual(actual_result_2,expected_result_2)



class TestTflApiUrlBuilder(unittest.TestCase):

	def setUp(self):
		# this is the url for getting arrivals for commondale station
		self.url_builder = TflApiUrlBuilder()
		self.expected_url = 'https://api.tfl.gov.uk/StopPoint/%7Bids%7D/Arrivals?ids=490012375E' \
						+'&app_id=7df32329&app_key=b13d2099c8c5b37c0cbbe29c7b37faae'


	def test_url_builder(self):
		action_category = 'StopPoint'
		action = '%7Bids%7D/Arrivals'
		station_id = '490012375E'
		
		url = self.url_builder.with_action_category(action_category).with_action(action) \
			.with_station_id(station_id).build_url()
		self.assertEqual(url, self.expected_url)

	def test_url_builder_for_commondale(self):
		url = self.url_builder.build_commondale_url()
		self.assertEqual(url, self.expected_url)



unittest.main(verbosity=2)