import asyncio
import websockets
from .slack.slackbot import SlackerAdaptor



class Bot:
	def __init__(self) -> None:
		self.slackbot = SlackerAdaptor()

		self.slackbot.send_message(text="좋... 좋아해요", channel="#general")

	def start_session(self):
		try:
			endpoint = self.slackbot.start_real_time_messaging_session()

			async def execute_bot():
				ws = await websockets.connect(endpoint)
				while True:
					receive_json = await ws.recv()
					#listener.handle(receive_json)
		except Exceoption as e:
			pass