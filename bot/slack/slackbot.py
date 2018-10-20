import configparser

from slacker import Slacker

class SlackerAdaptor(object):
	def __init__(self, channel=None, user=None):
		self.config = configparser.ConfigParser()
		self.config.read('bot/config/config.ini')
		
		self.slacker = Slacker(self.config['SLACK']['TOKEN'])
			
		self.channel = channel
		self.user = user

		
	def send_message(self, channel=None, text=None):
		if channel is None:
			channel = self.config['CHANNEL']['DEFAULT']
		else:
			channel = channel
		
		self.slacker.chat.post_message(text=text, channel=channel, as_user=True)

	def start_real_time_messaging_session(self):
		response = self.slacker.rtm.start()
		return response.body["url"]

