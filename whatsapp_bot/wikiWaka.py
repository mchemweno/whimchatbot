import wikipedia


def GetInfo(message):
    try:
        answer = wikipedia.summary(message, chars=655360, auto_suggest=True)

        print(answer)
    except:
        answer = "please rephrase your question well"

    return str(answer)

