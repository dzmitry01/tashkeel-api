from fastapi import FastAPI
from pydantic import BaseModel
from mishkal.tashkeel import TashkeelClass
import threading

app = FastAPI()

# instance واحد لكل thread
thread_local = threading.local()

def get_tashkeel():
    if not hasattr(thread_local, "tashkeel"):
        thread_local.tashkeel = TashkeelClass()
    return thread_local.tashkeel

class TextInput(BaseModel):
    text: str

@app.post("/tashkeel")
def tashkeel_text(input: TextInput):
    t = get_tashkeel()
    result = t.tashkeel(input.text)
    return {"original": input.text, "tashkeel": result}

@app.get("/")
def root():
    return {"message": "Tashkeel API is running!"}