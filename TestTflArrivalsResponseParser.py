import unittest
import json
from TflArrivalsResponseParser import *

class TestTflArrivalsResponseParser(unittest.TestCase):

	def test_parse_response(self):
		eample_response_file = open('example_response.json')
		response_string = eample_response_file.read()
		expected_result_file = open('expected_result.json')
		expected_result = json.loads(expected_result_file.read())

		responseParser = TflArrivalsResponseParser()		
		self.assertEqual(responseParser.get_formated_response(response_string), expected_result)


unittest.main()