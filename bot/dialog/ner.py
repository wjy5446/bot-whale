from ..utils.datahandler import DataHandler



class NameEntityRecognizer(object):
	class __NER:
		def __init__(self):
			self.data_handler = DataHandler()
			self.skills = self.data_handler.read_file("skills.json")['skill']

		def parse(self, text, items):
			list_ner = []

			for name, keywords in items.items():
				result = any([key in text for key in keywords])

				if result:
					list_ner.append(name)
			
			return list_ner

	instance = None

	def __init__(self):
		if not NameEntityRecognizer.instance:
			NameEntityRecognizer.instance = NameEntityRecognizer.__NER()

	def __getattr__(self, name):
		return getattr(self.instance, name)