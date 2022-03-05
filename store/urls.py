from django.contrib import admin
from django.urls import path , include
from store import views

urlpatterns = [
   
    path('' , views.storeList.as_view()) ,
    path('<str:pk>' , views.storeAccess.as_view()) ,
    path('image/', views.ProductImageView.as_view(), name='add-product-image'),
]