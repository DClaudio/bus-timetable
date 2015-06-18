class TflApiUrlBuilder:

	base_url = "https://api.tfl.gov.uk"
	app_id = "7df32329"
	app_key = "b13d2099c8c5b37c0cbbe29c7b37faae"


	def __init__(self, action_category):
		self.action_category = action_category

	def with_action(self, action):
		self.action = action
		return self

	def with_station_id(self, station_id):
		self.station_id = station_id
		return self

	def build_url(self):
		return self.base_url + '/' + self.action_category + '/' + self.action \
				+ '?ids=' + self.station_id + '&app_id=' + self.app_id \
				+ '&app_key=' + self.app_key