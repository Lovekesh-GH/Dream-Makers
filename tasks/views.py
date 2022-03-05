from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin
from .serializers import *
from .models import NormalTasks,SpecialTasks

# Create your views here.
class NotificationView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = NormalSerializer
    queryset = NormalTasks.objects.all()

    def get(self, request: Request):
        return self.list(request)

    def post(self , request , *args ,**kwargs):
        return self.create(request , *args , **kwargs)


class NotificationViewUpdate(GenericAPIView , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin):
    serializer_class = SpecialSerializer
    queryset = SpecialTasks.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
