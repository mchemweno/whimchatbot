import wikipedia


def GetInfo(message):
    try:
        answer = wikipedia.summary(message, sentences=20, auto_suggest=True)

        print(answer)
    except:
        answer = "please rephrase your question well"

    return str(answer)

