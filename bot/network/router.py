from ..slack.slackbot import SlackerAdaptor

class MsgRouter(object):
	def __init__(self):
		self.slackbot = SlackerAdaptor()

	def message_route(
		self,
		text: str = None,
		user: str = None,
		channel: str = None
	):

		if "안녕" in text:
			self.slackbot.send_message(text="안녕하세요 후훗")


