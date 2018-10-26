import os
import json



class DataHandler(object):
	def __init__(self):
		self.data_path = "data/"
		self.log_data_path = "log/data/"

	def read_file(self, filename):
		text = self.read_text(filename)
		if text == "":
			return {}
		else:
			return json.loads(text)

	def read_text(self, filename, filepath=None):
		if filepath is None:
			filepath = self.data_path
		path = os.path.join(filepath + filename)
		try:
			with open(path, "rb") as infile:
				return infile.read().decode('utf-8')
		except BaseException:
			return ""

	def write_file(self, filename, data):
		path = os.path.join(self.data_path + filename)
		with open(path, "w", encoding="utf-8") as outfile:
			json.dump(data, outfile)
		
