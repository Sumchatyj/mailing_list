from .models import Client, Message
import requests
import json
import time
from django.utils import timezone
from dotenv import load_dotenv
import os


load_dotenv("../.env/.env")
TOKEN = os.getenv("TOKEN")
URL = "https://probe.fbrq.cloud/v1/send/"
HEADERS = {"authorization": TOKEN}


def compare_dates(mailing):
    if mailing.start_date >= mailing.end_date:
        return False
    if mailing.end_date <= timezone.now():
        return False
    return True


def get_clients(mailing):
    if mailing.tag != "" and mailing.phone_code is not None:
        return Client.objects.filter(
            tag=mailing.tag, phone_code=mailing.phone_code
        )
    elif mailing.tag != "":
        return Client.objects.filter(tag=mailing.tag)
    elif mailing.phone_code is not None:
        return Client.objects.filter(phone_code=mailing.phone_code)
    return Client.objects.all()


def send_message(mailing, client):
    message = Message.objects.create(
        mailing=mailing,
        client=client,
    )
    endpoint = URL + str(message.pk)
    data = {
        "id": message.pk,
        "phone": client.phone,
        "text": mailing.text,
    }
    try:
        response = requests.post(
            endpoint, data=json.dumps(data), headers=HEADERS
        )
        if response.status_code == 200:
            message.status = True
            message.save()
        else:
            raise Exception("Error with POST request")
    except Exception as e:
        print(e)


def start_messaging(mailing):
    if compare_dates(mailing) is False:
        return False
    if mailing.start_date > timezone.now():
        delta = mailing.start_date - timezone.now()
        print(delta)
        time.sleep(delta.total_seconds())
    clients = get_clients(mailing)
    for client in clients:
        send_message(mailing, client)
        if timezone.now() > mailing.end_date:
            break
