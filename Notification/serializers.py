from rest_framework import serializers
from Notification.models import Notification

Notification_Fields = (
    "Text",
    "date",
    "start_time",
    "end_time",
    "notification_time",
)
class NotificationViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = Notification_Fields