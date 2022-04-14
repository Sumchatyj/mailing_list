from rest_framework import serializers
from .models import Client, Mailing
from .messaging import start_messaging
from .phone_code import get_phone_code


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("id", "phone", "phone_code", "tag", "timezone")

    def create(self, validate_data):
        client = Client.objects.create(**validate_data)
        get_phone_code(client)
        return client

    def update(self, instance, validated_data):
        instance.phone = validated_data.get("phone", instance.phone)
        instance.timezone = validated_data.get("timezone", instance.timezone)
        instance.tag = validated_data.get("tag", instance.tag)
        get_phone_code(instance)
        return instance


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = ("id", "start_date", "end_date", "text", "tag", "phone_code")

    def create(self, validate_data):
        mailing = Mailing.objects.create(**validate_data)
        start_messaging(mailing)
        return mailing

    def update(self, instance, validated_data):
        instance.start_date = validated_data.get(
            "start_date", instance.start_date
        )
        instance.end_date = validated_data.get("end_date", instance.end_date)
        instance.text = validated_data.get("text", instance.text)
        instance.tag = validated_data.get("tag", instance.tag)
        instance.phone_code = validated_data.get(
            "phone_code", instance.phone_code
        )
        start_messaging(instance)
        return instance
