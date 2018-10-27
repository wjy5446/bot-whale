import json
import random
from .slack.slackbot import SlackerAdaptor
from .skills.greeting import Greeting
from .utils.logger import FunctionLogger


class Behave(object):
	def __init__(self, slackbot=None):
		if slackbot is None:
			self.slackbot = SlackerAdaptor()
		else:
			self.slackbot = slackbot

		self.func_logger = FunctionLogger().get_logger()


	def greeting(self):
		self.func_logger.info(
			json.dumps({"functions": "greeting"})
		)

		greeting = Greeting()
		text = greeting.talk()
		self.slackbot.send_message(text=text)

	def weather(self):
		self.func_logger.info(
			json.dumps({"function": "weather"})
		)
		self.slackbot.send_message(text="날씨가 참 좋아요 !!")
