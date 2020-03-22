import wikipedia


def GetInfo(message):
    try:
        answer = wikipedia.summary(message, sentences=935, auto_suggest=True)
        # answer = wikipedia.page(title=None, pageid=100, auto_suggest=True, redirect=True, preload=False)

        print(answer)
    except:
        answer = "please rephrase your question well"

    return str(answer)
