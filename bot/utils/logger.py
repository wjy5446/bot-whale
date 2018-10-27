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


class MessageLogger(object):
	class __Logger:
		def __init__(self):
			self._logger = logging.getLogger("message")
			self._logger.setLevel(logging.INFO)
			formatter = logging.Formatter(
				"%(asctime)s > %(message)s"
			)

			now = datetime.datetime.now()

			dir_name = "./log/message"
			if not os.path.isdir(dir_name):
				os.makedirs(dir_name)

			fileHandler = logging.FileHandler(
				dir_name + "/" + now.strftime("%Y-%m-%d") + ".log"
			)

			fileHandler.setFormatter(formatter)
			self._logger.addHandler(fileHandler)

	instance = None

	def __init__(self):
		if not MessageLogger.instance:
			MessageLogger.instance = MessageLogger.__Logger()

	def get_logger(self):
		return self.instance._logger

class FunctionLogger(object):
	class __Logger:
		def __init__(self):
			self._logger = logging.getLogger("function")
			self._logger.setLevel(logging.INFO)
			formatter = logging.Formatter(
				"%(asctime)s > %(message)s"
			)

			now = datetime.datetime.now()

			dir_name = "./log/function"
			if not os.path.isdir(dir_name):
				os.makedirs(dir_name)

			fileHandler = logging.FileHandler(
				dir_name + "/" + now.strftime("%Y-%m-%d") + ".log"
			)

			fileHandler.setFormatter(formatter)
			self._logger.addHandler(fileHandler)

	instance = None

	def __init__(self):
		if not FunctionLogger.instance:
			FunctionLogger.instance = FunctionLogger.__Logger()

	def get_logger(self):
		return self.instance._logger








