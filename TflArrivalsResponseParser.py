import json

class TflArrivalsResponseParser:

	def parse_response(self, http_response):
		return json.loads(http_response)

	def get_formated_response(self, http_response):
		response = self.parse_response(http_response)
		filtered_response = map(self.filter_dictionary,response)
		sorted_response = sorted(filtered_response, key = lambda k: k['timeToStation'])
		return sorted_response

	def filter_dictionary(self, entry):
		return {
				'route': entry['lineName'],
				'destination': entry['destinationName'],
				'timeToStation': entry['timeToStation']
				}