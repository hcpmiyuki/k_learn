from fastapi import FastAPI
from .models.translate import Translate

app = FastAPI()

@app.get("/")
def index():
    return {"msg": "hello world"}

@app.post("/translate")
def translate(sentence: str):
    translator = Translate(sentence=sentence)
    word_translation = translator.word_translate()
    sentence_translation = translator.sentence_translate()
    return {
        "word_translation": word_translation,
        "sentence_translation": sentence_translation
    }