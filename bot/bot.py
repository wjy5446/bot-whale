import asyncio
import websockets
import time
from .slack.slackbot import SlackerAdaptor
from .network.listener import MsgListener



class Bot:
	def __init__(self) -> None:
		self.slackbot = SlackerAdaptor()

	def start_session(self):
		try:
			endpoint = self.slackbot.start_real_time_messaging_session()
			listener = MsgListener()

			async def execute_bot():
				ws = await websockets.connect(endpoint)
				while True:
					receive_json = await ws.recv()
					listener.handle(receive_json)

			loop = asyncio.new_event_loop()
			asyncio.set_event_loop(loop)
			asyncio.get_event_loop().run_until_complete(execute_bot())
			asyncio.get_event_loop().run_forever()


		except BaseException as e:
			print(e)
			self.slackbot.send_message(text="머리 아포..")
			time.sleep(5)
			self.start_session()
