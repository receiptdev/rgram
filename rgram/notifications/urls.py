from django.urls import path
from . import views

app_name = 'notification_url'

urlpatterns = [
    path("", view=views.Notifications.as_view(), name="notifications"),
]
