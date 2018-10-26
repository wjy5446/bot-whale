import json
import configparser

from .router import MsgRouter
from ..utils.logger import Logger

class MsgListener(object):
	def __init__(self) -> None:
		self.config = configparser.ConfigParser()
		self.config.read('./bot/config/config.ini')
		self.router = MsgRouter()
		self.logger = Logger().get_logger()


	def handle(self, msg: str) -> None:
		msg = json.loads(msg)

		if self.is_message(msg):
			if self.is_self(msg):
				self.handle_user_message(msg)


	def handle_user_message(self, msg) -> MsgRouter.message_route:
		self.router.message_route(
			text=msg.get("text"),
			user=msg.get("user"),
			channel=msg.get("channel")
		)
	
	def is_message(self, msg) -> bool:
		msg_type = msg.get("type", None)
		if msg_type == "message":
			return True
		else:
			return False

	def is_self(self, msg) -> bool:
		msg_user = msg.get("user", None)
		if msg_user == self.config["USER"]["USER_ID"]:
			return True
		else:
			return False

