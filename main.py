from fastapi import FastAPI, Request
from os import link
import lxml
import requests
from requests.api import request
import json
import re

def chatbot(message):
    ai = {
        "input": message,
        "botkey": "icH-VVd4uNBhjUid30-xM9QhnvAaVS3wVKA3L8w2mmspQ-hoUB3ZK153sEG3MX-Z8bKchASVLAo~",
        "channel": 7,
        "sessionid": 482070240,
        "client_name": "uuiprod-un18e6d73c-user-19422"
    }
    url = "https://icap.iconiq.ai/talk"
    response = requests.post(url, ai).json()
    return response["responses"]

app = FastAPI()
@app.get('/')
def root(request: Request):
    return {"root": request.url.hostname/docs}

@app.get('/chatbot')
async def chatbot(message: str):
    data = chatbot(message)
    return {'message': data}





