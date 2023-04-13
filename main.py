from fastapi import FastAPI, Request
from os import link
import lxml
import requests
import json
import re

def chatbotai(text):
    try:
        params= {
                    "uid":"52227b3dc5d3bebe",
                    "input":text,
                    "sessionid":"483822266",
                }
        url = "https://kuli.kuki.ai/cptalk"
        response = requests.post(url, params).json()
        return response["responses"]
    except Exception as e:
        return e

app = FastAPI()
@app.get('/')
def root(request: Request):
    return {"root": request.url.hostname}

@app.get('/{message}')
async def chatbot(message: str):
    data = chatbotai(message)
    return {'Reply': data}
