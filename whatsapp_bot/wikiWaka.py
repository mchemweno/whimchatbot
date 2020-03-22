import wikipedia


def GetInfo(message):
    try:
        answer = wikipedia.page(title=message, auto_suggest=True, redirect=True, preload=False)
        print(answer.content)
    except:
        answer = "please rephrase your question well"

    return answer.content
