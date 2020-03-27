from bs4 import BeautifulSoup
import wikipedia
from twilio.rest import Client


def getInfo(message):
    answer = ''
    try:
        answer = wikipedia.page(title=message, auto_suggest=True, redirect=True, preload=True)
        answerString = answer.content
    except:
        answerString = "please rephrase your question well"

    myImage = ''
    if answer != '':
        if answer.images[1]:
            myImage = answer.images[1]

    return {'myImage': myImage, 'answer': answerString}


def getSummary(message):
    pass
