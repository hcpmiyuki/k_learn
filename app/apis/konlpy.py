from konlpy.tag import Mecab

class Konlpy:
	def __init__(self):
		self.mecab = Mecab()
		self.forbid_pos_list = self.read_forbid_pos_list()

	def read_forbid_pos_list(self):
		with open('app/statics/forbid_pos_list.txt') as f:
			forbid_pos_list = f.read().split('\n')
		return forbid_pos_list

	def sentence_to_words(self, sentence):
		word_pos_list = self.mecab.pos(sentence)
		words = []
		for word_pos in word_pos_list:
			word = word_pos[0]
			pos = word_pos[1]
			if pos not in self.forbid_pos_list:
				words.append(word)
		return words
