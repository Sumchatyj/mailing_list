from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Client(models.Model):
    phone = models.IntegerField(
        unique=True,
        validators=[
            MinValueValidator(70000000000),
            MaxValueValidator(79999999999),
        ],
    )
    phone_code = models.IntegerField(
        null=True, validators=[MinValueValidator(100), MaxValueValidator(999)]
    )
    timezone = models.IntegerField(
        null=True, validators=[MinValueValidator(-12), MaxValueValidator(12)]
    )
    tag = models.CharField(max_length=64, blank=True)


class Mailing(models.Model):
    start_date = models.DateTimeField()
    text = models.TextField()
    tag = models.CharField(max_length=64, blank=True)
    phone_code = models.IntegerField(
        blank=True, null=True, validators=[MaxValueValidator(999)]
    )
    end_date = models.DateTimeField()


class Message(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    mailing = models.ForeignKey(
        Mailing, related_name="message", on_delete=models.CASCADE
    )
    client = models.ForeignKey(
        Client, related_name="message", on_delete=models.CASCADE
    )
