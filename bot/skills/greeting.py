import random
from ..utils.datahandler import DataHandler



class Greeting(object):

	def __init__(self):
		self.datahandler = DataHandler()
		self.dialog = self.datahandler.read_text("dialog/greeting.txt").split("\n")

	def talk(self):
		dialog_greeting = random.sample(self.dialog, 1)
		return dialog_greeting