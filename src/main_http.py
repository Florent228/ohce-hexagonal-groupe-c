from fastapi import FastAPI, Request
from pydantic import BaseModel
from domain.HorlogeSysteme import HorlogeSysteme
from langs.LangFactory import LangFactory
from domain.MirrorService import MirrorService

app = FastAPI()

time = HorlogeSysteme()
langue_factory = LangFactory()

class Word(BaseModel):
    word: str

@app.post("/")
def main(request: Request, word: Word):
    word = word.word
    code_langue = request.headers.get('Accept-Language')[0:2]
    language = langue_factory.create_lang(code_langue)
    mirror_service = MirrorService(language, time)

    mirror_service.setWord(word)

    response = {
        "greetings": mirror_service.greeting(),
        "word": mirror_service.getWord(),
        "palindrome": mirror_service.mirror(),
        "goodbye": mirror_service.goodbye()
    }

    return response