from django.shortcuts import render
from .models import Store
from .serializers import storeSerializer
from rest_framework.generics import GenericAPIView , CreateAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin , UpdateModelMixin , RetrieveModelMixin , DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class storeList(GenericAPIView , ListModelMixin , CreateModelMixin):
    serializer_class = storeSerializer
    queryset = Store.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self , request , *args ,**kwargs):
        return self.create(request , *args , **kwargs)

class storeAccess(GenericAPIView , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin):
    serializer_class = storeSerializer
    queryset = Store.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class ProductImageView(GenericAPIView , ListModelMixin , CreateModelMixin):
#     serializer_class = ProductImageSerializer
#     queryset = ProductImage.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self , request , *args ,**kwargs):
#         return self.create(request , *args , **kwargs)

