from bs4 import BeautifulSoup
import wikipedia


def getInfo(message):
    try:
        answer = wikipedia.page(title=message, auto_suggest=True, redirect=True, preload=True)
        # print(answer.content)
    except:
        return "please rephrase your question well"

    return answer.content



