
from django.urls import path

from .views import  NotificationViewUpdate, SNotificationView, SNotificationViewUpdate, NotificationView


urlpatterns = [
    path("", NotificationView.as_view()),
    path("<str:pk>/", NotificationViewUpdate.as_view()),
    path("special/", SNotificationView.as_view()),
    path("special/<str:pk>/", SNotificationViewUpdate.as_view()),
    
]