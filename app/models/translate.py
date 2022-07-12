from ..apis.konlpy import Konlpy
from ..apis.korean_dict import KoreanDict

class Translate:
    def __init__(self, sentence):
        self.tokenizer = Konlpy()
        self.sentence = sentence
        self.words = self.sentence_to_words()
        self.word_translator = KoreanDict()
    
    def sentence_to_words(self):
        words = self.tokenizer.sentence_to_words(self.sentence)
        return words
    
    def word_translate(self):
        results = []
        for word in self.words:
            res = self.word_translator.word_translate(word)
            results.append(res)
        return results
    
    def sentence_translate(self):
        pass