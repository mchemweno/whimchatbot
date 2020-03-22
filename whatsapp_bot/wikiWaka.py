from bs4 import BeautifulSoup
import wikipedia

def getInfo(message):
    try:
        # answer = wikipedia.page(title=message, auto_suggest=True, redirect=True, preload=True)
        # soup = BeautifulSoup(answer.content, 'html.parser')
        # text = soup.get_text()

        answer = wikipedia.summary(message, auto_suggest=True)
    except:
        return "please rephrase your question well"

    return answer


