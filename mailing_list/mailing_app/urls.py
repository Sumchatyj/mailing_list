from django.urls import path, include
from rest_framework import routers
from .views import (
    ClientViewSet,
    MailingViewSet,
    get_message_statistic,
    get_mailing_statistic,
)


router = routers.DefaultRouter()
router.register(r"clients", ClientViewSet)
router.register(r"mailing", MailingViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("message/<int:mailing_pk>/", get_message_statistic),
    path("mailing-stat/", get_mailing_statistic),
]
