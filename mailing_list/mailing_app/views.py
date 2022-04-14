from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Client, Mailing, Message
from .serializers import ClientSerializer, MailingSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


@api_view(["GET"])
def get_message_statistic(request, mailing_pk):
    try:
        mailing = Mailing.objects.get(pk=mailing_pk)
        sent_messages = len(
            Message.objects.filter(mailing=mailing.pk, status=True)
        )
        not_sent_messages = len(
            Message.objects.filter(mailing=mailing.pk, status=False)
        )
        data = {
            "mailing": mailing.pk,
            "sent_messages": sent_messages,
            "not_sent_messages": not_sent_messages,
        }
        return Response(data, status=status.HTTP_200_OK)
    except Exception:
        print("no mailing with this pk")
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_mailing_statistic(request):
    try:
        mailing = len(Mailing.objects.all())
        sent_messages = len(Message.objects.filter(status=True))
        not_sent_messages = len(Message.objects.filter(status=False))
        data = {
            "number_of_mailing": mailing,
            "number_of_sent_messages": sent_messages,
            "number_of_not_sent_messages": not_sent_messages,
        }
        return Response(data, status=status.HTTP_200_OK)
    except Exception:
        print("no mailing")
        return Response(status=status.HTTP_400_BAD_REQUEST)
