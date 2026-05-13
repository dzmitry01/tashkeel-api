from fastapi import FastAPI
from pydantic import BaseModel
from mishkal.tashkeel import TashkeelClass

app = FastAPI()
tashkeel = TashkeelClass()

class TextInput(BaseModel):
    text: str

def do_tashkeel(text: str) -> str:
    # نصنع instance جديد في كل مرة لتجنب مشكلة SQLite threads
    t = TashkeelClass()
    return t.tashkeel(text)

@app.post("/tashkeel")
def tashkeel_text(input: TextInput):
    result = do_tashkeel(input.text)
    return {"original": input.text, "tashkeel": result}

@app.get("/")
def root():
    return {"message": "Tashkeel API is running!"}