import six
from google.cloud import translate_v2 as translate

class GoogleTranslate:
	def __init__(self):
		self.client = translate.Client()

	def translate_sentence(self, sentence):
		if isinstance(sentence, six.binary_type):
			sentence = sentence.decode("utf-8")
		result = self.client.translate(sentence, target_language="ja")
		print(result)
		return result["translatedText"]
