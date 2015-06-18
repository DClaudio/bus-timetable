class TflApiUrlBuilder:

	base_url = "https://api.tfl.gov.uk"
	app_id = "7df32329"
	app_key = "b13d2099c8c5b37c0cbbe29c7b37faae"


	def with_action_category(self, action_category):
		self.action_category = action_category
		return self

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

	# custom method just for commondale bus station
	def build_commondale_url(self):		
		action_category = 'StopPoint'
		action = '%7Bids%7D/Arrivals'
		station_id = '490012375E'
		return self.with_action_category(action_category).with_action(action) \
			.with_station_id(station_id).build_url()