import json

class TflArrivalsResponseParser:

	def parse_response(self, http_response):
		return json.loads(http_response)

	def get_formated_response(self, http_response):
		response = self.parse_response(http_response)
		sorted_response = sorted(response, key = lambda k: k['timeToStation'])
		formated_resp = list(map(self.filter_dictionary, sorted_response))
		return formated_resp

	def filter_dictionary(self, entry):
		return {
				'route': entry['lineName'],
				'destination': entry['destinationName'],
				'timeToStation': self.format_seconds(entry['timeToStation'])
				}

	def format_seconds(self, seconds):
		m, s = divmod(seconds, 60)
		return '{0}:{1}'.format(m, s)

	# LCD - can fit only 16 characters per line
	def format_line(self, entry):
		return '{0:>{widht_0}} {1:>{widht_1}} {2}'.format(entry['route'], entry['timeToStation'], 
			entry['destination'][:6], widht_0=3, widht_1=5)