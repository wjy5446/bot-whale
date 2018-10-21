import logging
import os
import datetime



class Logger(object):
	class __Logger:
		def __init__(self):
			self._logger = logging.getLogger("crumbs")
			self._logger.setLevel(logging.INFO)
			formatter = logging.Formatter(
				"[%(levelname)s|%(filename)s:%(lineno)s %(asctime)s > %(message)s"
			)

			now = datetime.datetime.now()

			dir_name = "./log/activity/" + now.strftime("%Y-%m-%d")
			if not os.path.isdir(dir_name):
				os.makedirs(dir_name)

			fileHandler = logging.FileHandler(
				dir_name + "/Kino_" + now.strftime("%Y-%m-%d %H:%M") + ".log"
			)
			streamHandler = logging.StreamHandler()

			fileHandler.setFormatter(formatter)
			streamHandler.setFormatter(formatter)

			self._logger.addHandler(fileHandler)
			self._logger.addHandler(streamHandler)
	
	instance = None

	def __init__(self):
		if not Logger.instance:
			Logger.instance = Logger.__Logger()

	def get_logger(self):
		return self.instance._logger



