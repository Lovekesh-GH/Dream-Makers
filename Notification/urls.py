from django.urls import path
from Notification.views import NotificationView, NotificationViewUpdate

urlpatterns = [
    path('', NotificationView.as_view(),name="Notification"),
    path('<str:pk>' ,NotificationViewUpdate.as_view()) ,
]