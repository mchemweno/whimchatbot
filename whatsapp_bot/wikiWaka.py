import wikipedia


def GetInfo(message):
    try:
        answer = wikipedia.page(title=message, auto_suggest=True, redirect=True, preload=False)
        np = ''
        for i in answer.content:
            np = np + i
        print(np)
    except:
        np = "please rephrase your question well"

    return str(np)
