from fastapi import FastAPI, Request
from os import link
import lxml
import requests
import json
import re

def chatbotai(text):
    ai = {
        "input": text,
        "botkey": "icH-VVd4uNBhjUid30-xM9QhnvAaVS3wVKA3L8w2mmspQ-hoUB3ZK153sEG3MX-Z8bKchASVLAo~",
        "channel": 7,
        "sessionid": 482070240,
        "client_name": "uuiprod-un18e6d73c-user-19422",
        "id": "true"
    }
    url = "https://icap.iconiq.ai/talk"
    response = requests.post(url, ai).json()
    return response["responses"]

app = FastAPI()
@app.get('/')
def root(request: Request):
    return {"root": request.url.hostname}

@app.get('/chatbot')
async def chatbot(message: str):
    data = chatbotai(message)
    return {'Reply': data}





