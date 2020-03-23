from bs4 import BeautifulSoup
import wikipedia
from twilio.rest import Client


def getInfo(message):
    try:
        answer = wikipedia.page(title=message, auto_suggest=True, redirect=True, preload=True)
        answerString = answer.content
    except:
        return "please rephrase your question well"

    return answerString


def getSummary(message):
    pass


mystring = getInfo('Classes of computers')

start = 0
stop = 1600
step = 0
reference = 1600

for x in range(0, len(mystring)):
    step = step + 1
    if len(mystring) < 1600:
        print(mystring)
        break
    if step == reference:
        print(mystring[start:stop:])
        start += 1600
        stop+= 1600
        reference += 1600

    difference = (len(mystring)-stop)
    if difference < 1600:
        print(mystring[stop:])
        break
