import unittest
import json
from TflArrivalsResponseParser import *

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


unittest.main()