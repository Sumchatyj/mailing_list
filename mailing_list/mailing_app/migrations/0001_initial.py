# Generated by Django 3.2.3 on 2022-04-13 17:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "phone",
                    models.IntegerField(
                        unique=True,
                        validators=[
                            django.core.validators.MaxValueValidator(
                                99999999999
                            )
                        ],
                    ),
                ),
                (
                    "phone_code",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(999)
                        ]
                    ),
                ),
                (
                    "timezone",
                    models.IntegerField(
                        blank=True,
                        validators=[
                            django.core.validators.MaxValueValidator(999)
                        ],
                    ),
                ),
                ("tag", models.CharField(blank=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateTimeField()),
                ("text", models.TextField()),
                ("attributes", models.CharField(max_length=64)),
                ("end_date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("status", models.BooleanField(default=False)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="message",
                        to="mailing_app.client",
                    ),
                ),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="message",
                        to="mailing_app.mailing",
                    ),
                ),
            ],
        ),
    ]