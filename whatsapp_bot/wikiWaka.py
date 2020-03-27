from bs4 import BeautifulSoup
import wikipedia
from twilio.rest import Client


def getInfo(message):
    try:
        answer = wikipedia.page(title=message, auto_suggest=True, redirect=True, preload=True)
        answerString = answer.content
    except:
        return "please rephrase your question well"

    myImage = ''
    if answer.images[0]:
        myImage= answer.images[0]

    return {'myImage': myImage, 'answer': answerString}


def getSummary(message):
    pass


