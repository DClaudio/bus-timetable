import unittest
from TflArrivalsResponseParser import *

class TestTflArrivalsResponseParser(unittest.TestCase):

	def test_parse_response(self):
		eample_file = open('example_response.json')
		response_string = eample_file.read()
		expected_result = {'name': "test", 'number': 1}

		responseParser = TflArrivalsResponseParser()		
		self.assertEqual(responseParser.parse_response(response_string), expected_result)


unittest.main()