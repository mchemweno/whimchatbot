import wikipedia


def GetInfo(message):
    try:
        answer = wikipedia.summary(message, sentences=5)
        print(answer)
    except:
        answer = "please rephrase your question well"

    return answer
