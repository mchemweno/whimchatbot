from django.http import JsonResponse, HttpResponse
from . import wikiWaka

# Create your views here.
from rest_framework.decorators import api_view
from twilio.twiml.messaging_response import MessagingResponse


@api_view(['POST'])
def WhatsappBot(request):
    print(request.data)
    msg = request.data['Body']

    answer = wikiWaka.GetInfo(msg)

    resp = MessagingResponse()
    resp.message(answer)

    print(resp)
    return HttpResponse(resp)
