from django.http import JsonResponse, HttpResponse
from . import wikiWaka

# Create your views here.
from rest_framework.decorators import api_view
from twilio.twiml.messaging_response import MessagingResponse


@api_view(['POST'])
def WhatsappBot(request):
    print(request.data)
    msg = request.data['Body']

    answer = wikiWaka.getInfo(msg)

    resp = MessagingResponse()
    resp.message(answer)

    start = -1600
    stop = 0
    step = 1600

    for x in range(0, len(answer)):
        start = start + 1600
        stop = start + 1600

        if (stop == step):
            resp.message(answer[start:stop])

        step = step + 1600

    return HttpResponse(resp)


@api_view(['POST'])
def DeliveryStatus(request):
    print(request.data)

    return HttpResponse(status=200)
