import wikipedia
from html.parser import HTMLParser

def GetInfo(message):
    try:
        answer = wikipedia.page(title=message, auto_suggest=True, redirect=True, preload=False)
        print(type(answer.content))
    except:
        return "please rephrase your question well"

    return answer.content

