from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin
from tasks.serializers import NormalSerializer, SCompletedSerializer, CompletedSerializer, SpecialSerializer
from tasks.models import NormalTasks,SpecialTasks,Completedtasks, SCompletedtasks

# Create your views here.
class StaskView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = SpecialSerializer
    queryset = SpecialTasks.objects.all()

    def get(self, request: Request):
        return self.list(request)

    def post(self , request , *args ,**kwargs):
        return self.create(request , *args , **kwargs)


class StaskViewUpdate(GenericAPIView , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin):
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

class taskView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = NormalSerializer
    queryset = NormalTasks.objects.all()

    def get(self, request: Request):
        return self.list(request)

    def post(self , request , *args ,**kwargs):
        return self.create(request , *args , **kwargs)


class taskViewUpdate(GenericAPIView , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin):
    serializer_class = NormalSerializer
    queryset = NormalTasks.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SCompletedView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = SCompletedSerializer
    queryset = SCompletedtasks.objects.all()

    def get(self, request: Request):
        return self.list(request)

    def post(self , request , *args ,**kwargs):
        return self.create(request , *args , **kwargs)


class SCompletedViewUpdate(GenericAPIView , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin):
    serializer_class = SCompletedSerializer
    queryset = SCompletedtasks.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CompletedView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = CompletedSerializer
    queryset = Completedtasks.objects.all()

    def get(self, request: Request):
        return self.list(request)

    def post(self , request , *args ,**kwargs):
        return self.create(request , *args , **kwargs)


class CompletedUpdate(GenericAPIView , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin):
    serializer_class = CompletedSerializer
    queryset = Completedtasks.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



