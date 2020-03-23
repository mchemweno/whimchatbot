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

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hello! This is an editable text message. You are free to change it and write whatever you like.',
        to=request.data['From']
    )
    # resp = MessagingResponse()
    # resp.message(answer)

    return HttpResponse(status=200)


@api_view(['POST'])
def DeliveryStatus(request):
    print(request.data)

    return HttpResponse(status=200)
