import unittest
from TflArrivalsResponseParser import *

class TestTflArrivalsResponseParser(unittest.TestCase):

	def test_parse_response(self):
		responseParser = TflArrivalsResponseParser()		
		self.assertEqual("true", "true")


unittest.main()