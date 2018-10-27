import datetime
import configparser
import forecastio



class Weather(object):
	def __init__(self):
		self.config = configparser.ConfigParser()
		self.config.read('bot/config/config.ini')
		self.now_date_local = datetime.datetime.now()
			
	def tell_current_forecast(self):
		self.forecast = forecastio.load_forecast(self.config['API_DARKSKY'].get('API_DARKSKY'),
												self.config['POS_SEOUL'].get('LAT'),
												self.config['POS_SEOUL'].get('LNG'),
												)
		current_forecast = self.forecast.currently()

		current_summary = current_forecast.summary
		current_icon = current_forecast.icon
		current_time = current_forecast.time
		current_temperature = current_forecast.temperature
		current_precipProbability = current_forecast.precipProbability

		print(current_summary, current_icon, current_time, 
			current_temperature, current_precipProbability)

		return None

	def tell_tomorrow_forecast(self):
		dict_count_weather = {}
		
		tomorrow_local = self.now_date_local + datetime.timedelta(days=1)
		tomorrow_local = datetime.datetime(tomorrow_local.year, tomorrow_local.month, tomorrow_local.day, 6, 0, 0)

		forecast = forecastio.load_forecast(self.config['API_DARKSKY'].get('API_DARKSKY'),
												self.config['POS_SEOUL'].get('LAT'),
												self.config['POS_SEOUL'].get('LNG'),
												time=tomorrow_local
												)
		hourly_forecast = forecast.hourly()
		summary_weather = self.summary_daily_forecast(hourly_forecast)
		
		attachments_dict = {}
		attachments_dict['pretext'] = "내일 날씨 정보예요!!"
		attachments_dict['title'] = "내일 날씨"
		attachments_dict['text'] = """
		오전의 날씨: {weather_morning}, 온도 {temper_morning}, 습도 {humidity_morning}\n
		오후의 날씨: {weather_afternoon}, 온도 {temper_afternoon}, 습도 {humidity_afternoon}\n
		저녁의 날씨: {weather_night}, 온도 {temper_night}, 습도 {humidity_night}\n
		""".format(weather_morning=summary_weather['weather_morning'],
					weather_afternoon=summary_weather['weather_afternoon'],
					weather_night=summary_weather['weather_night'],
					temper_morning=summary_weather['avg_temp_morning'],
					temper_afternoon=summary_weather['avg_temp_afternoon'],
					temper_night=summary_weather['avg_temp_night'],
					humidity_morning=summary_weather['avg_hum_morning'],
					humidity_afternoon=summary_weather['avg_hum_afternoon'],
					humidity_night=summary_weather['avg_hum_night'])
		
		if len(summary_weather['list_rain_hour']) > 0:
			print(summary_weather['list_rain_hour'])
			rain_hour = " ".join(summary_weather['list_rain_hour'])
			dialog_rain_hour = "비는 {rain_hour}에 올테니 우산 준비해 나가세요".format(rain_hour=rain_hour)
			attachments_dict['text'] += dialog_rain_hour


		attachments = [attachments_dict]



		return attachments
		

	def tell_today_forecast(self):
		dict_count_weather = {}

		today_local = self.now_date_local
		today_local = datetime.datetime(today_local.year, today_local.month, today_local.day, 6, 0, 0)
	
		self.forecast = forecastio.load_forecast(self.config['API_DARKSKY'].get('API_DARKSKY'),
												self.config['POS_SEOUL'].get('LAT'),
												self.config['POS_SEOUL'].get('LNG'),
												time=today_local
												)
		hourly_forecast = self.forecast.hourly()
		summary_weather = self.summary_daily_forecast(hourly_forecast)

		print(summary_weather)

	def tell_asked_date_forecast(self, month, day, year=None, hour=None, minute=None, second=None):
		now = self.now_date
		
		if year is None:
			year = now.year

		if hour is None:
			hour = 12

		if minute is None:
			minute = 0

		if second is None:
			second = 0

		asked_date_local = datetime.datetime(year, month, day, hour, minute, second)

		self.forecast = forecastio.load_forecast(self.config['API_DARKSKY'].get('API_DARKSKY'),
												self.config['POS_SEOUL'].get('LAT'),
												self.config['POS_SEOUL'].get('LNG'),
												time=self.local2utc(asked_date)
												)
		asked_date_forecast = self.forecast.currently()

		print(asked_date_forecast)

	def summary_daily_forecast(self, hourly_datas):
		"""
        정보(주된 날씨만)
		오전 시간(6-12)
		오후 시간(12-18)
		저녁 시간(18-24)

		비 정보 만 출력
		"""
		dict_weather_info = {
							"weather_morning": {}, "weather_afternoon": {}, "weather_night": {},
							"avg_temp_morning": 0, "avg_temp_afternoon": 0, "avg_temp_night": 0,
							"avg_hum_morning": 0, "avg_hum_afternoon": 0, "avg_hum_night": 0, 
							"list_rain_hour": []
							
		}

		for data in hourly_datas.data:
			summary = data.summary
			temper = data.temperature
			humidity = data.humidity
			hour = self.utc2local(data.time).hour

			if 'Rain' in summary:
				dict_weather_info['list_rain_hour'].append(str(hour)) 

			if hour < 6:
				continue
			elif hour < 12:
				dict_weather = 'weather_morning'
				avg_temp = 'avg_temp_morning'
				avg_hum = 'avg_hum_morning'
			elif hour < 18:
				dict_weather = 'weather_afternoon'
				avg_temp = 'avg_temp_afternoon'
				avg_hum = 'avg_hum_afternoon'
			else:
				dict_weather = 'weather_night'
				avg_temp = 'avg_temp_night'
				avg_hum = 'avg_hum_night'				

			if summary in dict_weather_info[dict_weather]:
				dict_weather_info[dict_weather][summary] += 1
			else:
				dict_weather_info[dict_weather][summary] = 1
			dict_weather_info[avg_temp] += temper
			dict_weather_info[avg_hum] += humidity

		for k, v in dict_weather_info.items():
			if 'weather' in k:
				dict_weather_info[k] = sorted(v.items(), key=lambda x: x[1])[0][0]
			if 'temp' in k or 'hum' in k:
					dict_weather_info[k] = round(v / 6, 1)


		return dict_weather_info

	def utc2local(self, utc, offset=9):
		local = utc + datetime.timedelta(hours=offset)
		return local

	def local2utc(self, local, offset=9):
		utc = local - datetime.timedelta(hours=offset)
		return utc


if __name__ == "__main__":
	w = Weather()
	w.tell_tomorrow_forecast()