from fastapi import FastAPI, Request
from os import link
import lxml
import requests
import json
import re

def chatbotai(text):
    params= {
                "uid":"52227b3dc5d3bebe",
                "input":text,
                "sessionid":"483786864",
            }
    url = "https://kuli.kuki.ai/cptalk"
    response = requests.post(url, ai).json()
    return response["responses"]

app = FastAPI()
@app.get('/')
def root(request: Request):
    return {"root": request.url.hostname}

@app.get('/{message}')
async def chatbot(message: str):
    data = chatbotai(message)
    return {'Reply': data}





