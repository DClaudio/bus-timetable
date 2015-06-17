import json

class TflArrivalsResponseParser:

	def parse_response(self, http_response):
		return json.loads(http_response)

	def remove_unused_attr(self, data):
		

