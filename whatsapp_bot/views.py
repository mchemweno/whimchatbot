from django.http import HttpResponse
from twilio.rest import Client

from . import wikiWaka

# Create your views here.
from rest_framework.decorators import api_view
from twilio.twiml.messaging_response import MessagingResponse


@api_view(['POST'])
def WhatsappBot(request):
    print(request.data)
    msg = request.data['Body']

    answer = wikiWaka.getInfo(msg)

    account_sid = 'ACdc287d5d268548c5fb806a6d9b64f1c3'
    auth_token = 'b93c5358a6f88ce95bd35ab4e8648f81'
    client = Client(account_sid, auth_token)

    start = 0
    stop = 1600
    step = 0
    reference = 1600

    for x in range(0, len(answer)):
        step = step + 1
        if len(answer) < 1600:
            print(answer)
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=answer,
                to=request.data['From']
            )
            break
        if step == reference:
            print(answer[start:stop:])
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=answer[start:stop:],
                to=request.data['From']
            )
            start += 1600
            stop += 1600
            reference += 1600

        difference = (len(answer) - stop)
        if difference < 1600:
            print(answer[:stop:])
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=answer[:stop:],
                to=request.data['From']
            )
            break

    resp = MessagingResponse()
    resp.message("Thank you for using Whim")

    return HttpResponse(resp)


@api_view(['POST'])
def DeliveryStatus(request):
    # print(request.data)
    #
    # return HttpResponse(status=200)
    pass
