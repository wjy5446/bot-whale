import json

from ..behave import Behave
from ..slack.slackbot import SlackerAdaptor
from ..dialog.ner import NameEntityRecognizer
from ..utils.logger import Logger
from ..utils.logger import MessageLogger

class MsgRouter(object):
	def __init__(self):
		self.slackbot = SlackerAdaptor()
		self.msg_logger = MessageLogger().get_logger()
		self.behave = Behave(self.slackbot)

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
	
		ner = NameEntityRecognizer()

        # Check - skills
		skill_keywords = {k: v["keyword"] for k, v in ner.skills.items()}
		list_func = ner.parse(text, skill_keywords)
	
		if len(list_func) > 0:
			for func_name in list_func:
				self.__call_skills(func_name)		


	def __call_skills(self, func_name: str):
		getattr(self.behave, func_name)()
		return
