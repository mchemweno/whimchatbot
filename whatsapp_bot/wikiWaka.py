from bs4 import BeautifulSoup
import wikipedia


def getInfo(message):
    try:
        answer = wikipedia.page(title=message, auto_suggest=True, redirect=True, preload=True)
        answerString = answer.content[:1600:]
        print(answerString)
    except:
        return "please rephrase your question well"

    return answerString


