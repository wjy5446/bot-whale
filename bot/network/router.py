import json

from ..slack.slackbot import SlackerAdaptor
from ..utils.logger import Logger
from ..utils.logger import MessageLogger

class MsgRouter(object):
	def __init__(self):
		self.slackbot = SlackerAdaptor()
		self.msg_logger = MessageLogger().get_logger()

	def message_route(
		self,
		text: str = None,
		user: str = None,
		channel: str = None
	):
		if text is not None:
			self.msg_logger.info(
				json.dumps({"channel": channel, "user": user, "text": text})
			)

		if "안녕" in text:
			self.slackbot.send_message(text="안녕하세요 후훗")


