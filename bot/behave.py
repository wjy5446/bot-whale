from .slack.slackbot import SlackerAdaptor



class Behave(object):
	def __init__(self, slackbot=None):
		if slackbot is None:
			self.slackbot = SlackerAdaptor()
		else:
			self.slackbot = slackbot

	def greeting(self):
		self.slackbot.send_message(text="안녕하세요 후훗")

	def weather(self):
		self.slackbot.send_message(text="날씨가 참 좋아요 !!")
