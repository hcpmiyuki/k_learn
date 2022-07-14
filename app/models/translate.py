from ..apis.konlpy import Konlpy
# from ..apis.korean_dict import KoreanDict
from ..apis.google_translation import GoogleTranslate

class Translate:
    def __init__(self, sentence):
        self.tokenizer = Konlpy()
        self.sentence = sentence
        self.words = self.sentence_to_words()
        # self.word_translator = KoreanDict()
        self.sentence_translator = GoogleTranslate()
    
    def sentence_to_words(self):
        words = self.tokenizer.sentence_to_words(self.sentence)
        return words
    
    def word_translate(self):
        results = []
        for word in self.words:
            res = self.sentence_translator.translate_sentence(word)
            results.append({word: res})
        return results
    
    def sentence_translate(self):
        result = self.sentence_translator.translate_sentence(self.sentence)
        return {self.sentence: result}